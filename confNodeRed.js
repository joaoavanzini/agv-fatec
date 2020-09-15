
str = JSON.stringify(msg.payload);
par = JSON.parse(str);
obj = new Array();
obj = {}

obj["distance"] = par.right[0]["distance"]
obj["datetime"] = par.right[0]["datetime"]

msg.payload = JSON.stringify(obj);
msg.payload = JSON.parse(msg.payload);

return msg;
