from abc import ABCMeta,abstractmethod

# 抽象产品角色，以什么样的表现去使用
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass

# 产品角色
class Alipay(Payment):
    def __init__(self,use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self,money=0):
        if self.use_huabei:
            print(f"花呗支付{money}元")
        else:
            print(f"支付宝余额支付{money}元")

# 产品角色
class WechartPay(Payment):
    def pay(self,money):
        print(f"微信余额支付{money}元")

# 工厂类角色
class PaymentFactory:
    def create_payment(self,method):
        if method == "Alipay":
            return Alipay()
        elif method == "WechatPay":
            return WechartPay()
        elif method == "HuabeiPay":
            return Alipay(use_huabei=True)
        else:
            raise TypeError('No such payment named %s' % method)