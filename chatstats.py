import datetime as dt

def parseMessages(msgs):
    
    arr_msgs = msgs.split("\n")

    arr_msgs_dicts = []

    last_msg = None

    while last_msg is None and len(arr_msgs) > 0:
        last_msg = messageToDict(arr_msgs.pop(0))

    if last_msg is None:
        print("Doesn't look like these are whatsApp messages")
        return []

    for msg in arr_msgs:
        maybe_msg = messageToDict(msg)

        if maybe_msg is None:
            last_msg['message'] += "\n" + msg
        else:
            arr_msgs_dicts.append(last_msg)
            last_msg = maybe_msg

    arr_msgs_dicts.append(last_msg)
    
    return arr_msgs_dicts


def messageToDict(msg):

    try:
        timestamp, _, rest = msg.partition(" - ")
        name, _, rest = rest.partition(": ")

        return {
                'date': dt.datetime.strptime(timestamp, "%d/%m/%Y, %I:%M %p"),
                'name': name,
                'message': rest
            }
    except ValueError:
        return None

def countBySender(arr_msgs_dicts):
    
    counts = {}

    for msg in arr_msgs_dicts:
        if msg['name'] not in counts:
            counts[msg['name']] = 1
        else:
            counts[msg['name']] += 1

    sorted_dict = {k: v for k, v in sorted(
        counts.items(),
        key=lambda x: x[1], 
        reverse=True
    )}

    return sorted_dict