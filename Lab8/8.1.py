import catalog as ct

# 7.1
note = ct.read_data('..//Lab7/note.txt')
media_note = ct.calc_media(note)
ct.show_details(media_note)

# 7.2
ct.show_details_note(note)

# 7.3
order_note = ct.cust_sort(media_note, 1, True)
ct.show_prem(order_note)

# 7.4
teze = ct.read_data('..//Lab7/teze.txt')
media_gen = ct.cust_sort(ct.media_gen(note, teze))
ct.show_details(media_gen, 'media_gen.txt')

