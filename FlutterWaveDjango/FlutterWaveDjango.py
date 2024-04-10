from rave_python import Rave, RaveExceptions, Misc

class FlutterWaveDjango:
    def __init__(self, inProduction:bool, public:str, secret: str):
        self.public:str = public
        self.secret:str = secret
        try:
            if inProduction == False: 
                self.rave:str = Rave(publicKey=self.public, secretKey=self.secret, usingEnv=False, production=False,)
            else:
                self.rave: Rave = Rave(publicKey=self.public, secretKey=self.secret, usingEnv=True, production=True)
            self.card = self.rave.Card
            self.payout = self.rave.Transfer
        except Exception as e:
            error = {"error": str(e), "statusCode": 400}
            print(error)
            
        

    def cardPaymentInitiate(self, payload):
        try:
            self.charge = self.card.charge(payload)
            return {"success": self.charge, "statusCode": 200}

        except RaveExceptions.CardChargeError as e:
            return {"card_error": str(e), "statusCode": 400}

        except RaveExceptions.TransactionValidationError as e:
            return {"validation_error": str(e), "statusCode": 400}

        except RaveExceptions.TransactionVerificationError as e:
            return {"verify_error": str(e), "statusCode": 400}
    
    def validate3DCardPayment(self):
        pass
    def cardPinVerification(self, pin, payload, charge):

        try:
            if charge["suggestedAuth"]:
               
                arg = Misc.getTypeOfArgsRequired(charge["suggestedAuth"])
                if arg == "pin":
                    Misc.updatePayload(charge["suggestedAuth"], payload, pin=pin)
                    charge = self.card.charge(payload)
                    
                    return {"message": charge, "status":"valid","statusCode": 200}

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
        
        
