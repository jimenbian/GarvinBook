import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#import data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init_op = tf.initialize_all_variables()
saver = tf.train.Saver()


# Train the model and save the model to disk as a model.ckpt file
# file is stored in the same directory as this python script is started

with tf.Session() as sess:
    sess.run(init_op)
    for i in range(50000):
        batch_xs, batch_ys = mnist.train.next_batch(1)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        
    save_path = saver.save(sess, "model1.ckpt")
    print ("Model saved in file: ", save_path)
