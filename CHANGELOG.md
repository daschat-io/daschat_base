### :label: Add or update types

* Added the `agent_id`, `agent_name` fields to the `MessageSchema` schema. In the future it will allow to register in the log who wrote the message sent to the contact.
* Added new webhook type `CHAT_FORWARDED` in `WebhookTypesEnum` for when the chat is transferred to another agent or bot.

### :construction: Work in progress

* Added module `dc_abc_channel.py` with abstract class `ChannelBase` for channels plugins.
