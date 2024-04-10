from rave_python import Rave, RaveExceptions, Misc
from decouple import config
from rest_framework import status
from dotenv import load_dotenv


load_dotenv()

class FlutterWaveDjango:
    def __init__(self, isProduction:bool, public:str, secret: str) -> None:
        self.public:str = public
        self.secret:str = secret
        if isProduction == False: 
            self.rave:str = Rave(publicKey=self.public, secretKey=self.secret, usingEnv=False, production=False,)
        else:
            self.rave: Rave = Rave(publicKey=self.public, secretKey=self.secret, usingEnv=True, production=True)
            
        self.card = self.rave.Card
        self.payout = self.rave.Transfer

    def cardPaymentInitiate(self, payload):
        try:
            self.charge = self.card.charge(payload)
            return {"success": self.charge, "statusCode": status.HTTP_200_OK}

        except RaveExceptions.CardChargeError as e:
            return {"card_error": str(e), "statusCode": status.HTTP_400_BAD_REQUEST}

        except RaveExceptions.TransactionValidationError as e:
            return {"validation_error": str(e), "statusCode": status.HTTP_400_BAD_REQUEST}

        except RaveExceptions.TransactionVerificationError as e:
            return {"verify_error": str(e), "statusCode": status.HTTP_400_BAD_REQUEST}
    
    def validate3DCardPayment(self):
        pass
    def cardPinVerification(self, pin, payload, charge):

        try:
            if charge["suggestedAuth"]:
               
                arg = Misc.getTypeOfArgsRequired(charge["suggestedAuth"])
                if arg == "pin":
                    Misc.updatePayload(charge["suggestedAuth"], payload, pin=pin)
                    charge = self.card.charge(payload)
                    
                    return {"message": charge, "status":"valid","statusCode": status.HTTP_200_OK}

                # elif arg == "address":
                #     Misc.updatePayload(res["suggestedAuth"], payload, address=address)
                #     charge = self.card.charge(payload)
                #     return charge
                
                else:
                    return {
                        "message": "unable to initiate payment",
                        "status":"invalid",
        
                    }
            elif charge["suggestedAuth"] is None:
                return {
                    "message": "3-D card processssing",}
        except RaveExceptions.TransactionValidationError as e:
               
                return {
                "message": str(e),
                "status":"invalid",

            }

        except RaveExceptions.TransactionVerificationError as e:
            
            return {
                "message": str(e),
                "status":"unverify",

            }

    def cardOTPVerification(self, isValidationRequired, reference, otp):
        try:
            if isValidationRequired:
                validate = self.card.validate(reference, otp)
                return {"message": validate,"status":"verified"}

        except RaveExceptions.TransactionValidationError as e:
            return {
                "message": str(e),
                "status":"invalid",

            }

        except RaveExceptions.TransactionVerificationError as e:
            return {
                "message": str(e),
                "status":"unverify",

            }

    def cardPaymentVerify(self, txRef):
        return self.card.verify(txRef)

    def payoutUser(self, userAccountDetails):
        try:
            return self.payout.initiate(transferDetails=userAccountDetails)
        except RaveExceptions.IncompletePaymentDetailsError as e:
            return {"message": str(e)}

    def fetchVerifyPayout(self, reference):
        try:
            return self.payout.fetch(reference)
        except RaveExceptions.TransferFetchError as e:
            return {"message": str(e)}

    def fetchAllSuccessPayout(self):
        try:
            return self.payout.fetch()
        except RaveExceptions.TransferFetchError as e:
            return {"message": str(e)}

    def fetchAllCashout(self):
        try:
            return self.payout.all()
        except RaveExceptions.TransferFetchError as e:
            return {"message": str(e)}

    def fetchAccountBalance(self):
        try:
            return self.payout.getBalance("NGN")
        except RaveExceptions.TransferFetchError as e:
            return {"message": str(e)}
        
        
