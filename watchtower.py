from piston.steem import Steem
import pprint
pp = pprint.PrettyPrinter(indent=2)
steem = Steem(wif="Posting_WIF_Here")
ignored = ["comment", "vote", "custom_json", "pow2", "account_create"]
for c in steem.rpc.block_stream():
    try:
        tx = tx = c['transactions'][0]['operations'][0]  
        if(tx[0] not in ignored):
            pp.pprint(tx)
    except:
        pass


