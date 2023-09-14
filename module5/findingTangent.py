# Solve the problem of finding the tangent of the angle alpha
# given the sine of alpha and the cosine of alpha and
# add event logging to the "app.log" file.

# Catching the resulting sine and cosine values should be implemented using the "info" level.
# In the case of successful finding of the tangent of the alpha angle,
# logging should be with the "debug" level.
# In the event that cosine alpha = 0,
# logging should be with the "warning" level and the notification:
# "The cosine of the angle alpha = 0. The tangent is not defined.".
# In the event that the tangent is not defined,
# logging should be with the "critical" level and the notification:
#     "The tangent of the angle alpha is not defined.".

# tan(α) = sin(α) / cos(α)
import math
import logging


logging.basicConfig(level=logging.DEBUG, filename="app.log",filemode="w")


def findingTangent(sin_alpha, cos_alpha):
    logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    try:
        tan_αlpha = sin_alpha / cos_alpha
        message = f"The value of the tangent of the angle alpha is found = {tan_αlpha}"
        logging.debug(message)
    except ZeroDivisionError:
        message = "The cosine of the angle alpha = 0. The tangent is not defined."
        logging.warning(message)
    except:
        message = "The tangent of the angle alpha is not defined."
        logging.critical(message)


findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)
