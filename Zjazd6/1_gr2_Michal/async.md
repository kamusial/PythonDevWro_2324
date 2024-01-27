```mermaid
sequenceDiagram
    actor user
    user ->> Internet: youtube
    activate Internet    
    Internet ->> user: masz
    deactivate Internet
      
    user ->> Internet: netflix
    activate Internet
    Internet ->> user: masz
    deactivate Internet

```

```mermaid
sequenceDiagram
    actor user
    user ->> Internet: youtube
    user ->> Internet: netflix
    activate Internet
    Internet ->> user: masz
    deactivate Internet

```

