def play(sample_dict, step_num):
    for tracks in range(8):
        if sample_dict[tracks][1]["mode"] == "drum":
            for x in range(8):
                if sample_dict[tracks][0][x]["steps"][step_num - 1][0]:
                    try:
                        sample_dict[tracks][0][x]["sample"].stop()
                        sample_dict[tracks][0][x]["sample"].play()
                    except AttributeError:
                        pass
        elif sample_dict[tracks][1]["mode"] == "instrument":
            for x in range(8):
                try:
                    if sample_dict[tracks][0][x]["steps"][step_num - 1][1]:
                        pass
                    else:
                        sample_dict[tracks][0][x]["sample"].stop()
                except AttributeError:
                    pass
                if sample_dict[tracks][0][x]["steps"][step_num - 1][0]:
                    try:
                        sample_dict[tracks][0][x]["sample"].play()

                    except AttributeError:
                        pass