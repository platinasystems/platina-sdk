from platina_sdk.utils import get, post, put, delete, post_multipart, put_multipart
from .urls import *

def enable_mfa(conn: dict, data: dict) -> dict:
    """
    Enable MFA
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {"otp":"123456"} otp not required for the first request
    [Returns]
        (dict) Response: {"seed":"S3PFRG5VS7NQIZLI","qrCode":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV4AAAFeAQAAAADlUEq3AAACoUlEQVR4Xu2ZO5IqMQxFRREQzhJ6KSyte2kshSUQElCjpyMZ8DRthproBVcBLuxjglv6WZh/bjdb77wxwb0J7k1wb4J7E9yb4N4E9/YX+GrYnmXe+fXrfPSd+2U6zd95UpTgLfgrPr738XEyvp3N4tvFjktu+iJ4DLfjUHZ3M67GYpMHHOIfBf8K+9lm447jopjgz+GH3LEdQS74V9gzuqFK58Vvh4juCnkXPIYN24fcpMIfS54UJXgDbnYlFdYdL2rujwX3xw+dp1OFtS+1YJeAN11U8BN2cuAOTz2ylwLfDuxTle9yC96AwylDUjukzpxyJxJjVBjLhkbwCM5WOSWFgoai0FBh4kzwEA57hDW+SayTJr2JL/gtDBUFOFU+uhkuOjf3FTyCqSkZ3UmFb9I/Q1kLcsEjuCI4O+alNspTHbl5jwgew1MVk2homBXEcTM6GcFv4RT4im+Gpz4HVfMu0+QseAhXFWFdsorEu7eWIOy1pgh+wClwk9S4kzonlaM+wWM44nimd6mFqwiM1VNO8Aj2erVlkFNFHnLnnWkd3YKfMMpWx0xiNEZTaDxlkNMZCh7BCOyt36vEyEKQ59XXciz4obNxnGFt5ZRWm1Va1qlA8AqGsjYQTadE7q0JleA1jFOe00VjmZks+71GFyV4C679Jml76fLutRyWrnQW/AOOulETqoWqPLnzjctZYRISvAU3awJTWmZmBVmHX3QW3MNs0CpHWN9TYYZ1vOFoqjNNCt6G2//dKFsZ0fiFqVsEj+AQmE6GQG75MZe0dScjeAPm6DkyqMRIE1gmeAw7VCZG/kwriinpOroF97AT3SxLe7VBxWaTW/AQxhctXfQ+K0DuDOv8BcEj+DMT3Jvg3gT3Jrg3wb0J7k1wb/8L/A8Z2Xz93UgWmAAAAABJRU5ErkJggg=="}
    """
    return post(conn, PCC_USER_MANAGEMENT + "/user/mfa/enable", data)

def disable_mfa(conn: dict, data: dict) -> dict:
    """
    Disable MFA
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {"otp":"123456"}
    [Returns]
        (dict) Response: result of the operation
    """
    return post(conn, PCC_USER_MANAGEMENT + "/user/mfa/disable", data)

def reset_mfa(conn: dict, data: dict) -> dict:
    """
    Reset MFA
    [Args]
        (dict) conn: Connection dictionary obtained after logging in
        (dict) data: {"username":"admin", "source":"https://10.2.71.54:9999/gui/mfaReset"} in the first request
        (dict) Data: {"username":"admin", "otp":"4441756"} in the second request to complete the procedure
    [Returns]
        (dict) Response: result of the operation
    """
    return post(conn, PCC_USER_MANAGEMENT + "/user/mfa/reset", data)
