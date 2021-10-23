## 0.12.1 (2021-10-23)

### :label: Add or update types

* Created `version.py` for package version info.
* Created `types.py` to be the global type and class definition center.
* Added new enum type `MessageDispatchEnum` in `WebhookTypesEnumtypes.py`.
* Added the `dispatch` field to the `MessageSchema` schema. In the future it will allow to select wich module of **DasChat** will process the message.
