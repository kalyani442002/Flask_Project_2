from flask import Flask
FAI=Flask(__name__)

@FAI.route('/wish/<name>')
def hello(name):
    return 'How are you {}'.format(name)

if __name__=='__main__':
    FAI.run(debug=True,port=5000,host='192.168.132.1')