from gmail import *


gmail = GMail('tophuonglinh12@gmail.com','Chunchun123')
msg = Message('title',to='tophuonglinh12@gmail.com',html='1234')
gmail.send(msg)