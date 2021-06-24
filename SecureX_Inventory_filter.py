import sys, datetime, hashlib, hmac, base64, codecs, json
(body,secret,observable_value) = sys.argv[1:]

### Uncomment for testing
#f = open('body_noquery.json')
#f = open('body_1query.json')
#f = open('body.json')
#body=json.load(f)
#observable_value="4.4.4.4/32"

def generate_auth(method,path,body,secret):
    content_type='application/json'
    time_fmt = '%Y-%m-%dT%H:%M:%S+0000'
    timestamp = datetime.datetime.utcnow().strftime(time_fmt)
    checksum = ""
    if method in ("POST","PUT","DELETE"): checksum = hashlib.sha256(body.encode('utf-8')).hexdigest()
    signer = hmac.new(codecs.encode(secret,'latin-1'), digestmod=hashlib.sha256)
    signer.update((method + '\n').encode('utf-8'))
    signer.update((path + '\n').encode('utf-8'))
    signer.update((checksum + '\n') .encode('utf-8'))
    signer.update((content_type + '\n').encode('utf-8'))
    signer.update((timestamp + '\n').encode('utf-8'))
    signature = base64.b64encode(signer.digest())
    authorization = signature.decode('utf-8')
    return (timestamp,checksum,authorization)

item_found = False
action_required = False
body = json.loads(body)
app_scope_id = body['app_scope_id']
filter_id = body['id']

## Search for IP being reported in current NotABogon Inventory Filter
try:
    if body['short_query']['filters']:
        print("gotcha_with_body")
        for i,item in enumerate(body['short_query']['filters']):
            print(item)
            if item['field']=="ip" and item['value']==observable_value:
                item_found=True
                action_required=False
                print('Found!')
            else:
                action_required=True
                skip=False
except KeyError:
    if 'short_query' in body and body['short_query']['type'] != 'none':
        print("gotcha with part body")
        if body['short_query']['value']==observable_value:
            item_found=True
            action_required=False
            print('Found!')
        else:
            old_entry=body.pop('short_query')
            action_required=True
            skip=False
            print(old_entry)
    else:
        action_required=True
        query = {
                "type": "subnet",
                "field": "ip",
                "value": observable_value+'/32'
            }
        body['short_query'] = query
        skip=True

## If IP not found in current inventory filter then add it to current filter
if item_found==False and action_required==True and not skip:
    query = {
                "type": "subnet",
                "field": "ip",
                "value": observable_value+'/32'
            }
    try:
        body['short_query']['filters'].append(query)
    except KeyError:
        body['short_query']={}
        body['short_query']['type'] = "or"
        body['short_query']['filters'] = []
        body['short_query']['filters'].append(query)
        body['short_query']['filters'].append(old_entry)


(update_body,update_timestamp,update_checksum,update_auth)=(None,None,None,None)
if action_required==True:
    if body['query']:
        del body['query']
        update_body=json.dumps(body)
        (update_timestamp,update_checksum,update_auth)=generate_auth('PUT','/openapi/v1/filters/inventories/'+filter_id,update_body,secret)
print(update_body,update_timestamp,update_checksum,update_auth)
print()