from piston.steem import Steem
steem = Steem(wif="WIF")
ignored = ["comment", "vote", "custom_json", "pow2"]
for c in steem.rpc.block_stream():
    try:
        tx = tx = c['transactions'][0]['operations'][0]  
        if(tx[0] not in ignored):
            print(tx)
    except:
        pass


