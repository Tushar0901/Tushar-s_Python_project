hostname = random.choice(ip_list)

for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Sending a packet, checking its reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        break
    elif reply.type == 3:
        # Final destnation
        print "Done!", reply.src
        break
    else:
        # Almost there
        print "%d hops away: " % i , reply.src
