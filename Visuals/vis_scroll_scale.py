import config

def vis_scroll_change_scale(scroll_input):
    #print(scroll_input)
    if config.logarithmic_scroll:
        pass
        config.scale_divis = config.scale_divis - scroll_input * (config.scale_divis/50)
        config.scale = 1 / config.scale_divis

    else:
        config.scale_divis = config.scale_divis - scroll_input * 10**3  #anmerkung für späteres ich: evtl so machen, dass die änderung von der momentanen größe abhängt?
        config.scale = 1 / config.scale_divis
    #print(config.scale)
