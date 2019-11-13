import secure_smtpd
import logging

# Implment this interface with an actual
# methodlogy for validating credentials, e.g.,
# lookup credentials for a user in Redis.
class FakeCredentialValidator(object):
    
    def validate(self, username, password):
        
        logger = logging.getLogger( secure_smtpd.LOG_NAME )
        
        if username == 'bcoe' and password == 'foobar':
            return True
        return False