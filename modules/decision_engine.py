from typing import Dict

ACCESS_THRESHOLD = 0.9
CHALLENGE_THRESHOLD = 0.7
BLOCK_THRESHOLD = 0.0

def decision_engine(confidence_score: float, new_device: bool = False, new_ip: bool = False) -> Dict[str, str]:
    """
    Decide authentication action based on confidence score and new device/IP flags.
    - New device or new IP is considered light if confidence_score is already high.
    - Returns decision, reason, and alert_level.
    """
    # Light exceptions for new device or IP
    if confidence_score >= ACCESS_THRESHOLD:
        return {
            "decision": "access_granted",
            "reason": "High confidence in genuine behavior, new device/IP is acceptable.",
            "alert_level": "success"
        }
    elif confidence_score >= CHALLENGE_THRESHOLD:
        # Step-up authentication for minor anomalies or new device/IP
        reason = "Minor deviations detected"
        if new_device or new_ip:
            reason += "; new device/IP detected, consider verification"
        else:
            reason += "; step-up authentication recommended"
        return {
            "decision": "challenge_user",
            "reason": reason,
            "alert_level": "warning"
        }
    else:
        return {
            "decision": "block_access",
            "reason": "Significant anomaly detected; session blocked.",
            "alert_level": "danger"
        }

