# get-distant-access


How to access a machine from the outside when the firewall doesn't allow you to nc, ssh, telnet, ftp, etc but when the machine has access to Internet ? In this repository I present my solution which consists in a Telegram bot that runs locally on the machine I want to run commands on from distance. When issued a given command, the bot fetches the commands to run from a gist on  Github, writes the commands in a script and execute the script. The results of each commands in returned in the chat as a text message. 

This allows to execute commands without accessing the machine, the only traffic generated is between Github and Telegram which are probably allowed and wouldn't triggered any alert to the sysadmins. Note that you can replace Github and/or Telegram with any solution that would be better for example Slack, pastbin, Discord, etc. 
