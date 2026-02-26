```mermaid
stateDiagram-v2
    [*] --> Available
    Available --> InUse: bookRoom()
    InUse --> Available: Checkout / Time expired
    InUse --> Cancelled: cancelBook()
    Cancelled --> Available: Cleanup / Re-release
```