#!/usr/bin/python
#coding=utf8
import random
import jpype
#import chardet
#随机生成指定位数随机的参数，
def random_test(digit):
    f=''
    for i in range(0,digit):
        a  = random.randint(97, 122)#小写字母
        b  = random.randint(65, 90)#大写字母
        c  = random.randint(48, 57)#数字
        d=[a,b,c]
        e = chr(d[random.randint(0, 2)])
        f=f+e
        i+=1#可有 可无(强迫症，去除i警告)
    return f
#print random_test(20)
jvmPath = jpype.getDefaultJVMPath()
B=jpype.startJVM(jpype.getDefaultJVMPath(), '-Djava.class.path=E:/pyhton_pay/pay_fun/sdk_pass.jar')
def pay_sdk_decrypt(s):
    password = "fb887dcf145644058c3739e977f5a854"
    #s ="8QrYTDZCxnI1rCBAETOFuZFxCqhiD/NKtCuDRTmDS+k="
    salt = [126, 27, 33, 64, 57, 76, 87, 98]
    X = jpype.JClass('com.pay.common.PBECoder')
    Y= jpype.JClass('com.pay.common.Coder')
    #res=str((X.decrypt(Y.decryptBASE64(s),password,salt))).encode('utf-8')
    try: 
        res=str((X.decrypt(Y.decryptBASE64(s),password,salt))).encode('gbk')
    except Exception:
        try: 
            res=str((X.decrypt(Y.decryptBASE64(s),password,salt))).encode('utf8')
        except Exception,e:
            res=e
    
    #print chardet.detect(res)
    return res
def pay_sdk_decrypt_test(s):
    password = "12345"
    #s ="8QrYTDZCxnI1rCBAETOFuZFxCqhiD/NKtCuDRTmDS+k="
    salt = [126, 27, 33, 64, 57, 76, 87, 98]
    X = jpype.JClass('com.pay.common.PBECoder')
    Y= jpype.JClass('com.pay.common.Coder')
    res=str(X.decrypt(Y.decryptBASE64(s),password,salt)).encode('utf-8')
    #print chardet.detect(res)
    return res


#print pay_sdk_decrypt_test('R2fI+1CbILwwmcL2jAI+d4qLbjf2OkpfV75fG5IxMYs7ATadnsI2oiDq+QfoPsMnl3nQdzothkt+WCRu70aPfZZ4yz3byK91hlLXyrL2edfVl0+MDrgkbnwj5gC5AZH1kKBwWUcWcI11LTbXtO6l+KKuO0fHZt6p5+3paQ7YyHA29r4NcZBthsERGt9DzW7bOgh+WWSHzGA=')
#print pay_sdk_decrypt('6BK39DO8DenF2yEz9apqkTiwK4RmsoDjNs6XiAMGtkROoNSrAHs7Uu23N899Lk6OLM9FqOjSjoQA8aVzyVB+K52fkIb4ukG7+4MOsopRZwpjzOWsqa+DuJoIPomO3oXJ3yeJT5F/WzXaKgxzQhYqZZd3Gc86AFxwK7MMap5SvdBa6rYkMHR1XN+tirrqegOmWhWK8vo+R2it6fGuY/OqIIss3ytnPsvjYgjbdhbZgSk7uvOqlH2OD7nvSASEnUqv7AqhZo9R9j9mig63Y4w8zGy8tlF8d1xJX3Z8ES2Cn6J65AYWz99pSDt0X/jHp9IatMtICmHc6NJjJzPxCJVbqjCQ/B5v2cLb2ujtHTM1XD2ddfEn9aOaZFgAkYA1dFrUZjXPDySEG0LFKeea8TUjunCc5o0Eips3tsuau3J1oVLTBO1yo8aGJlaKIihGz2eyVDqVs4ZQu9qyrGJywyCAb4FNdicBnTIVQweUWSKFGuXgO/M0q3Lq4RUXvwo+VAam2yDa4fDHAfTwdzUn5cGhzA==')

print pay_sdk_decrypt_test('R2fI+1CbILwwmcL2jAI+d4qLbjf2OkpfQjUVgkKONlVJFiQFCEbS1gay0A8WhYQUEoU+8Xxeqsyui/SeZYmCw91ur0hfq5Nybc57eJdIjfv6ZHHCSvaKvCeBiRCziWYQ3F/Sp+OfqGHsBbtQNSz9UGUIOwrXZCWsPwtjq8qu2PvX+LGJRJkpuAf1uO2zChcIfrwUa742mtP5uF7UszarJOLkxk/8Hync8uwij2re3g18HxOAtEYNt53t6ncCtp7wguRzCUtHakk94razYA03ggLea7v4BVPliJo4l9GCAGhuFFeLFFVNXJMYT6Wu8261A8e/1ZmrJ4bZjaytjzKWJMhcQX6y7gMsNUSSOQeDYQMHG6TqHtQ6cJuHZAt4Deykga8UqW8bImKt1y2xiCl94v5XMg+tDoc3IB/YNVP95mnyFjKHHOO4CQPkYIZ5lIYHKU08unOIieI77vq5lP9nlhvRXRm8V0Ejylkcg7Y1OwYIqM54+/u8OK2HvJfFDkk7LxXfhnUy8FprnpsC4YTtiQ==')


