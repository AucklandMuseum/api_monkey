{"filter":false,"title":"MOATweet.py","tooltip":"/MOATweet.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":56,"column":31},"end":{"row":56,"column":32},"action":"remove","lines":["1"],"id":357}],[{"start":{"row":56,"column":31},"end":{"row":56,"column":32},"action":"insert","lines":["c"],"id":358},{"start":{"row":56,"column":32},"end":{"row":56,"column":33},"action":"insert","lines":["a"]},{"start":{"row":56,"column":33},"end":{"row":56,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"remove","lines":["1"],"id":359}],[{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":["c"],"id":360},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":["a"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":7},"end":{"row":53,"column":37},"action":"remove","lines":[" if os.stat('1.jpg').st_size > 3000000:","                print ('resize image')","                image_file = 'cat.jpg'","                img_org = Image.open(image_file)","                width_org, height_org = img_org.size","                factor = 0.75","                width = int(width_org * factor)","                height = int(height_org * factor)","                img5 = img_org.resize((width, height), Image.ANTIALIAS)","                ext = \".jpg\"","                img5.save(\"moaresized\" + ext)","                api.update_with_media('moaresized.jpg', str(tweet))","                print (tweet)","                #wait three hours","                time.sleep(10800)    "],"id":361}],[{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"remove","lines":["1"],"id":362}],[{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"insert","lines":["c"],"id":363},{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["a"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":364},{"start":{"row":41,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["",""]},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""]},{"start":{"row":43,"column":0},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":39,"column":7},"end":{"row":59,"column":49},"action":"insert","lines":[" ","                        try:","                            if os.stat('1.jpg').st_size > 3000000:","                                print 'resize image'","                                image_file = '1.jpg'","                                img_org = Image.open(image_file)","                                width_org, height_org = img_org.size","                                factor = 0.75","                                width = int(width_org * factor)","                                height = int(height_org * factor)","                                img5 = img_org.resize((width, height), Image.ANTIALIAS)","                                ext = \".jpg\"","                                img5.save(\"resized\" + ext)","                                api.update_with_media('resized.jpg', str(tweet))","                                print (tweet)","                                #wait three hours","                                time.sleep(10800)","                            else:","                                api.update_with_media('1.jpg', str(tweet))","                                print (tweet)","                                #wait three hours"],"id":365}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"remove","lines":["        "],"id":366},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"remove","lines":["        "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"remove","lines":["        "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"remove","lines":["        "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"remove","lines":["        "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":8},"action":"remove","lines":["        "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"remove","lines":["        "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"remove","lines":["        "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"remove","lines":["        "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"remove","lines":["        "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"remove","lines":["        "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"remove","lines":["        "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"remove","lines":["        "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":8},"action":"remove","lines":["        "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":8},"action":"remove","lines":["        "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":8},"action":"remove","lines":["        "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"remove","lines":["        "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"remove","lines":["        "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"remove","lines":["        "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"remove","lines":["        "]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"remove","lines":["        "],"id":367},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"remove","lines":["        "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"remove","lines":["        "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"remove","lines":["        "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"remove","lines":["        "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":8},"action":"remove","lines":["        "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"remove","lines":["        "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"remove","lines":["        "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"remove","lines":["        "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"remove","lines":["        "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"remove","lines":["        "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"remove","lines":["        "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"remove","lines":["        "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":8},"action":"remove","lines":["        "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":8},"action":"remove","lines":["        "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":8},"action":"remove","lines":["        "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"remove","lines":["        "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"remove","lines":["        "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"remove","lines":["        "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"remove","lines":["        "]}],[{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"remove","lines":["."],"id":368},{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["c"]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"remove","lines":["j"]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["a"]},{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"remove","lines":["p"]},{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["j"],"id":369},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["p"]}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["."],"id":370}],[{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"remove","lines":["1"],"id":371}],[{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"remove","lines":["1"],"id":372}],[{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["c"],"id":373},{"start":{"row":43,"column":31},"end":{"row":43,"column":32},"action":"insert","lines":["a"]},{"start":{"row":43,"column":32},"end":{"row":43,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":51,"column":34},"end":{"row":51,"column":35},"action":"insert","lines":["c"],"id":374},{"start":{"row":51,"column":35},"end":{"row":51,"column":36},"action":"insert","lines":["a"]},{"start":{"row":51,"column":36},"end":{"row":51,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":52,"column":46},"end":{"row":52,"column":47},"action":"insert","lines":["c"],"id":375},{"start":{"row":52,"column":47},"end":{"row":52,"column":48},"action":"insert","lines":["a"]},{"start":{"row":52,"column":48},"end":{"row":52,"column":49},"action":"insert","lines":["t"]}],[{"start":{"row":57,"column":39},"end":{"row":57,"column":40},"action":"remove","lines":["1"],"id":376}],[{"start":{"row":57,"column":39},"end":{"row":57,"column":40},"action":"insert","lines":["c"],"id":377},{"start":{"row":57,"column":40},"end":{"row":57,"column":41},"action":"insert","lines":["a"]},{"start":{"row":57,"column":41},"end":{"row":57,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":59,"column":0},"end":{"row":68,"column":52},"action":"remove","lines":["                #wait three hours    ","","","","","","","","        ","        api.update_with_media('cat.jpg', str(tweet))"],"id":378},{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "],"id":379}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["#"],"id":380}],[{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"remove","lines":["        "],"id":381},{"start":{"row":60,"column":8},"end":{"row":61,"column":0},"action":"remove","lines":["",""]},{"start":{"row":60,"column":0},"end":{"row":60,"column":8},"action":"remove","lines":["        "]},{"start":{"row":59,"column":33},"end":{"row":60,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":59,"column":33},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":382},{"start":{"row":60,"column":0},"end":{"row":60,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":60,"column":16},"end":{"row":61,"column":47},"action":"insert","lines":["except TweepError:","                            print \"tweet error\""],"id":383}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"remove","lines":["        "],"id":384}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"insert","lines":["        "],"id":385}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"remove","lines":["        "],"id":386}],[{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"remove","lines":[" "],"id":387},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"remove","lines":[" "]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"remove","lines":[" "]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":16},"action":"insert","lines":["        "],"id":388}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "],"id":389},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"insert","lines":["        "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":8},"action":"insert","lines":["        "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"insert","lines":["        "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"insert","lines":["        "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"insert","lines":["        "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"insert","lines":["        "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"insert","lines":["        "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"insert","lines":["        "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":8},"action":"insert","lines":["        "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":8},"action":"insert","lines":["        "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"remove","lines":[" "],"id":390}],[{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":[" "],"id":391}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":24},"action":"remove","lines":["        "],"id":392}],[{"start":{"row":56,"column":12},"end":{"row":56,"column":16},"action":"insert","lines":["    "],"id":393}],[{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "],"id":394},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"insert","lines":["        "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":[" "],"id":395}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"insert","lines":["        "],"id":396}],[{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"remove","lines":[" "],"id":397}],[{"start":{"row":61,"column":27},"end":{"row":61,"column":28},"action":"remove","lines":[" "],"id":398},{"start":{"row":61,"column":26},"end":{"row":61,"column":27},"action":"remove","lines":[" "]},{"start":{"row":61,"column":25},"end":{"row":61,"column":26},"action":"remove","lines":[" "]},{"start":{"row":61,"column":24},"end":{"row":61,"column":25},"action":"remove","lines":[" "]}],[{"start":{"row":61,"column":16},"end":{"row":61,"column":24},"action":"remove","lines":["        "],"id":399}],[{"start":{"row":61,"column":16},"end":{"row":61,"column":24},"action":"insert","lines":["        "],"id":400}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":16},"action":"remove","lines":["        "],"id":401}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":16},"action":"insert","lines":["        "],"id":402}],[{"start":{"row":60,"column":0},"end":{"row":61,"column":43},"action":"remove","lines":["                except TweepError:","                        print \"tweet error\""],"id":403}],[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "],"id":404},{"start":{"row":39,"column":7},"end":{"row":40,"column":0},"action":"remove","lines":["",""]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]}],[{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "],"id":405},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":[" "]}],[{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"remove","lines":[" "],"id":406},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":[" "]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"remove","lines":[" "]},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"remove","lines":[" "]},{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"remove","lines":[" "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":[" "]},{"start":{"row":38,"column":40},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":38,"column":40},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":407},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":58,"column":41},"end":{"row":58,"column":42},"action":"insert","lines":["."],"id":408}],[{"start":{"row":58,"column":42},"end":{"row":58,"column":46},"action":"insert","lines":["time"],"id":409}],[{"start":{"row":58,"column":42},"end":{"row":58,"column":46},"action":"remove","lines":["time"],"id":410},{"start":{"row":58,"column":41},"end":{"row":58,"column":42},"action":"remove","lines":["."]}],[{"start":{"row":58,"column":41},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":411},{"start":{"row":59,"column":0},"end":{"row":59,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":59,"column":24},"end":{"row":60,"column":47},"action":"insert","lines":["except TweepError:","                            print \"tweet error\""],"id":412}],[{"start":{"row":59,"column":16},"end":{"row":59,"column":24},"action":"remove","lines":["        "],"id":413},{"start":{"row":59,"column":8},"end":{"row":59,"column":16},"action":"remove","lines":["        "]}],[{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"remove","lines":[" "],"id":414},{"start":{"row":60,"column":26},"end":{"row":60,"column":27},"action":"remove","lines":[" "]},{"start":{"row":60,"column":25},"end":{"row":60,"column":26},"action":"remove","lines":[" "]},{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"remove","lines":[" "]},{"start":{"row":60,"column":16},"end":{"row":60,"column":24},"action":"remove","lines":["        "]},{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"remove","lines":["        "]}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":16},"action":"insert","lines":["        "],"id":415}],[{"start":{"row":27,"column":143},"end":{"row":27,"column":144},"action":"insert","lines":[" "],"id":416},{"start":{"row":27,"column":144},"end":{"row":27,"column":145},"action":"insert","lines":["#"]},{"start":{"row":27,"column":145},"end":{"row":27,"column":146},"action":"insert","lines":["c"]},{"start":{"row":27,"column":146},"end":{"row":27,"column":147},"action":"insert","lines":["a"]},{"start":{"row":27,"column":147},"end":{"row":27,"column":148},"action":"insert","lines":["t"]},{"start":{"row":27,"column":148},"end":{"row":27,"column":149},"action":"insert","lines":["s"]},{"start":{"row":27,"column":149},"end":{"row":27,"column":150},"action":"insert","lines":["o"]},{"start":{"row":27,"column":150},"end":{"row":27,"column":151},"action":"insert","lines":["f"]}],[{"start":{"row":27,"column":151},"end":{"row":27,"column":152},"action":"insert","lines":["A"],"id":417},{"start":{"row":27,"column":152},"end":{"row":27,"column":153},"action":"insert","lines":["u"]},{"start":{"row":27,"column":153},"end":{"row":27,"column":154},"action":"insert","lines":["c"]},{"start":{"row":27,"column":154},"end":{"row":27,"column":155},"action":"insert","lines":["k"]},{"start":{"row":27,"column":155},"end":{"row":27,"column":156},"action":"insert","lines":["l"]},{"start":{"row":27,"column":156},"end":{"row":27,"column":157},"action":"insert","lines":["a"]},{"start":{"row":27,"column":157},"end":{"row":27,"column":158},"action":"insert","lines":["n"]},{"start":{"row":27,"column":158},"end":{"row":27,"column":159},"action":"insert","lines":["d"]}],[{"start":{"row":27,"column":159},"end":{"row":27,"column":160},"action":"insert","lines":[" "],"id":418}],[{"start":{"row":27,"column":159},"end":{"row":27,"column":160},"action":"remove","lines":[" "],"id":419}],[{"start":{"row":27,"column":149},"end":{"row":27,"column":150},"action":"remove","lines":["o"],"id":420}],[{"start":{"row":27,"column":149},"end":{"row":27,"column":150},"action":"insert","lines":["O"],"id":421}],[{"start":{"row":59,"column":19},"end":{"row":59,"column":20},"action":"remove","lines":["p"],"id":422},{"start":{"row":59,"column":18},"end":{"row":59,"column":19},"action":"remove","lines":["e"]},{"start":{"row":59,"column":17},"end":{"row":59,"column":18},"action":"remove","lines":["e"]},{"start":{"row":59,"column":16},"end":{"row":59,"column":17},"action":"remove","lines":["w"]},{"start":{"row":59,"column":15},"end":{"row":59,"column":16},"action":"remove","lines":["T"]}],[{"start":{"row":60,"column":35},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":423},{"start":{"row":61,"column":0},"end":{"row":61,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":16},"action":"remove","lines":["        "],"id":424}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["e"],"id":425},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":["x"]},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["c"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["e"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["p"]}],[{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":["t"],"id":426}],[{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":[" "],"id":427}],[{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["√"],"id":428}],[{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"remove","lines":["√"],"id":429}],[{"start":{"row":61,"column":15},"end":{"row":61,"column":33},"action":"insert","lines":["UnicodeEncodeError"],"id":430}],[{"start":{"row":61,"column":33},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":431},{"start":{"row":62,"column":0},"end":{"row":62,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":62,"column":8},"end":{"row":62,"column":16},"action":"insert","lines":["        "],"id":432}],[{"start":{"row":62,"column":16},"end":{"row":62,"column":17},"action":"insert","lines":["p"],"id":433},{"start":{"row":62,"column":17},"end":{"row":62,"column":18},"action":"insert","lines":["r"]},{"start":{"row":62,"column":18},"end":{"row":62,"column":19},"action":"insert","lines":["i"]},{"start":{"row":62,"column":19},"end":{"row":62,"column":20},"action":"insert","lines":["n"]},{"start":{"row":62,"column":20},"end":{"row":62,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":62,"column":21},"end":{"row":62,"column":22},"action":"insert","lines":[" "],"id":434}],[{"start":{"row":62,"column":22},"end":{"row":62,"column":24},"action":"insert","lines":["\"\""],"id":435}],[{"start":{"row":62,"column":23},"end":{"row":62,"column":24},"action":"insert","lines":["u"],"id":436},{"start":{"row":62,"column":24},"end":{"row":62,"column":25},"action":"insert","lines":["n"]},{"start":{"row":62,"column":25},"end":{"row":62,"column":26},"action":"insert","lines":["i"]},{"start":{"row":62,"column":26},"end":{"row":62,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":62,"column":26},"end":{"row":62,"column":27},"action":"remove","lines":["d"],"id":437}],[{"start":{"row":62,"column":26},"end":{"row":62,"column":27},"action":"insert","lines":["c"],"id":438},{"start":{"row":62,"column":27},"end":{"row":62,"column":28},"action":"insert","lines":["o"]},{"start":{"row":62,"column":28},"end":{"row":62,"column":29},"action":"insert","lines":["d"]},{"start":{"row":62,"column":29},"end":{"row":62,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":62,"column":30},"end":{"row":62,"column":31},"action":"insert","lines":[" "],"id":439},{"start":{"row":62,"column":31},"end":{"row":62,"column":32},"action":"insert","lines":["e"]},{"start":{"row":62,"column":32},"end":{"row":62,"column":33},"action":"insert","lines":["r"]},{"start":{"row":62,"column":33},"end":{"row":62,"column":34},"action":"insert","lines":["r"]},{"start":{"row":62,"column":34},"end":{"row":62,"column":35},"action":"insert","lines":["o"]},{"start":{"row":62,"column":35},"end":{"row":62,"column":36},"action":"insert","lines":["r"]}],[{"start":{"row":61,"column":33},"end":{"row":61,"column":34},"action":"insert","lines":[":"],"id":440}],[{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"remove","lines":["        "],"id":441}],[{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"insert","lines":["        "],"id":442}],[{"start":{"row":21,"column":16},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":443},{"start":{"row":22,"column":0},"end":{"row":22,"column":10},"action":"insert","lines":["          "]}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":[" "],"id":444},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["t"],"id":445},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["r"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":[":"],"id":446}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "],"id":447},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":8},"action":"insert","lines":["        "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":8},"action":"insert","lines":["        "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":8},"action":"insert","lines":["        "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":8},"action":"insert","lines":["        "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"insert","lines":["        "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":8},"action":"insert","lines":["        "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":8},"action":"insert","lines":["        "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":8},"action":"insert","lines":["        "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"insert","lines":["        "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"insert","lines":["        "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"insert","lines":["        "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"insert","lines":["        "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":8},"action":"insert","lines":["        "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":8},"action":"insert","lines":["        "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":8},"action":"insert","lines":["        "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"insert","lines":["        "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":8},"action":"insert","lines":["        "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":61,"column":43},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":448},{"start":{"row":62,"column":0},"end":{"row":62,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":62,"column":24},"end":{"row":63,"column":43},"action":"insert","lines":["                except Error:","                        print \"tweet error\""],"id":449}],[{"start":{"row":62,"column":38},"end":{"row":62,"column":39},"action":"remove","lines":[" "],"id":450}],[{"start":{"row":62,"column":38},"end":{"row":62,"column":39},"action":"remove","lines":[" "],"id":451},{"start":{"row":62,"column":37},"end":{"row":62,"column":38},"action":"remove","lines":[" "]},{"start":{"row":62,"column":36},"end":{"row":62,"column":37},"action":"remove","lines":[" "]},{"start":{"row":62,"column":35},"end":{"row":62,"column":36},"action":"remove","lines":[" "]},{"start":{"row":62,"column":34},"end":{"row":62,"column":35},"action":"remove","lines":[" "]},{"start":{"row":62,"column":33},"end":{"row":62,"column":34},"action":"remove","lines":[" "]},{"start":{"row":62,"column":32},"end":{"row":62,"column":33},"action":"remove","lines":[" "]},{"start":{"row":62,"column":24},"end":{"row":62,"column":32},"action":"remove","lines":["        "]}],[{"start":{"row":62,"column":16},"end":{"row":62,"column":24},"action":"remove","lines":["        "],"id":452}],[{"start":{"row":62,"column":23},"end":{"row":62,"column":24},"action":"insert","lines":["I"],"id":453},{"start":{"row":62,"column":24},"end":{"row":62,"column":25},"action":"insert","lines":["O"]}],[{"start":{"row":62,"column":23},"end":{"row":62,"column":30},"action":"remove","lines":["IOError"],"id":454},{"start":{"row":62,"column":23},"end":{"row":62,"column":30},"action":"insert","lines":["IOError"]}],[{"start":{"row":66,"column":0},"end":{"row":67,"column":43},"action":"insert","lines":["except IOError:","                        print \"tweet error\""],"id":455}],[{"start":{"row":66,"column":0},"end":{"row":66,"column":8},"action":"insert","lines":["        "],"id":456}],[{"start":{"row":67,"column":16},"end":{"row":67,"column":24},"action":"remove","lines":["        "],"id":457}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":42,"column":53},"end":{"row":42,"column":53},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":157,"mode":"ace/mode/python"}},"timestamp":1596495087731,"hash":"55bf99543bf4e48d16a237a17c05cb6cef65b6f2"}