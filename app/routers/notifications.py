from fastapi import APIRouter

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

notifications = [
    {
        "id": 1,
        "title": "Vendor Approved",
        "message": "Vendor ABC Technologies has been approved.",
        "status": "Unread"
    },
    {
        "id": 2,
        "title": "Purchase Order Created",
        "message": "Purchase Order PO-1001 has been created.",
        "status": "Unread"
    }
]


@router.get("/")
def get_notifications():
    return notifications


@router.get("/{notification_id}")
def get_notification(notification_id: int):
    for notification in notifications:
        if notification["id"] == notification_id:
            return notification
    return {"message": "Notification not found"}


@router.put("/{notification_id}/read")
def mark_as_read(notification_id: int):
    for notification in notifications:
        if notification["id"] == notification_id:
            notification["status"] = "Read"
            return {
                "message": "Notification marked as read",
                "notification": notification
            }
    return {"message": "Notification not found"}


@router.delete("/{notification_id}")
def delete_notification(notification_id: int):
    for notification in notifications:
        if notification["id"] == notification_id:
            notifications.remove(notification)
            return {"message": "Notification deleted successfully"}
    return {"message": "Notification not found"}