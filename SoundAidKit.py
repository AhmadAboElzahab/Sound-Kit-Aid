from experta import *
from tkinter import *
from tkinter import messagebox



def Answer(word):
    app = Tk()
    app.title("Answer")
    app.iconbitmap(r'Images\SoundKitAid.ico')
    app.resizable(0, 0)
    ws = app.winfo_screenwidth()
    wh = app.winfo_screenheight()
    w = 650
    h = 450
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(bg="#141414")

    text = Text(app, width=80, height=27, border=0, relief=RAISED, bg="#141414", fg="white",
                font=("Jetbrains Mono", 10))
    text.insert(INSERT, 'The Answer is\n' + word)
    text.config(state=DISABLED)
    text.pack(expand=1, fill=BOTH)
   
    app.mainloop()


c = ""


def ok(app, v):
    global c
    c = v.get()
    if (c == ""):
        messagebox.showwarning('Check Warning', 'Please Check Before You Go on')
    else:
        app.destroy()


def test(question, answers):
    global c
    c = ""

    app = Tk()
    app.title("Sound Kit Aid")
    app.iconbitmap(r'Images\SoundKitAid.ico')
    app.resizable(0, 0)
    ws = app.winfo_screenwidth()
    wh = app.winfo_screenheight()

    w = 650
    h = 450
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(bg="#141414")

    text = Label(app, text=question, bg='#141414', fg='white', font=("Jetbrains Mono", 14)).pack(pady=10)

    v = StringVar()
    b = Button(app, text="Next", font=("jetbrains mono", 30), relief='flat', highlightthickness=0, bd=0, bg="#350c35",
               fg="white", command=lambda: ok(app, v)).place(x=250, y=300)

    for i in range(len(answers)):
        Radiobutton(app, text=answers[i], variable=v, indicator=0, value=answers[i]
                    , relief='flat', highlightthickness=0, bd=0
                    , bg="#141414", fg="#bb1433", font=("Jetbrains Mono", 15)).pack(pady=5)

    
    app.mainloop()

    return c


class Sound_Kit_Aid(KnowledgeEngine):
    @Rule()
    def Start(self):
        x = test("Why Do you want to use the system?", ['personal use', 'event organizer'])
        self.declare(Fact(action=x))

    # personal use
    @Rule(Fact(action='personal use'))
    def personal_use(self):
        x = test("Type of use?", ['content maker', 'music production'])
        self.declare(Fact(action=x))

    # personal use content maker
    @Rule(Fact(action='content maker'))
    def content_maker(self):
        x = test("do you have any equipment?", ['yes', 'no'])
        self.declare(Fact(content_maker_action=x))

    @Rule(Fact(content_maker_action='no'))
    def content_maker_equipment_no(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_action=x))

    @Rule(Fact(content_maker_action='high'))
    def content_maker_equipment_Budget_high(self):
        Answer(
            "\nMicrophone:Shure SM7B\nHeadset:Sennheiser PC 373D\nPC:ROG Zephrus M16(2022)\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_action='low'))
    def content_maker_equipment_low(self):
        Answer(
            "\nMicrophone:Sony ECM-CS3\nHeadset:SteelSeries Arctis 1\nPC:Lenovo Y520\nRecomended Softwere:open brodcaster software")

    # question about pc
    @Rule(Fact(content_maker_action='yes'))
    def content_maker_equipment_pc(self):
        x = test("Do you have A Personal Computer?", ['yes', 'no'])
        self.declare(Fact(content_maker_pc_action=x))

    @Rule(Fact(content_maker_pc_action='yes'))
    def content_maker_equipment_pc_mic(self):
        x = test("Do You have a microphone?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_pc_mic_action=x))

    @Rule(Fact(content_maker_equipment_pc_noMic_headset_action='yes'))
    def content_maker_equipment_pc_noMic_Headset(self):
        x = test("What is your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_pc_noMic_Headset_budget_action=x))

    @Rule(Fact(content_maker_equipment_pc_noMic_Headset_budget_action='high'))
    def content_maker_equipment_pc_noMic_Headset_budget_high(self):
        Answer("\nMicrophone:Shure SM7B\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_pc_noMic_Headset_budget_action='low'))
    def content_maker_equipment_pc_noMic_Headset_budget_low(self):
        Answer("\nMicrophone:Sony ECM-CS3\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_pc_mic_action='no'))
    def content_maker_equipment_pc_noMic(self):
        x = test("Do You have a Headset?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_pc_noMic_headset_action=x))

    @Rule(Fact(content_maker_equipment_pc_noMic_headset_action='no'))
    def content_maker_equipment_pc_noMic_noHeadset(self):
        x = test("What is your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_pc_noMic_noHeadset_budget_action=x))

    @Rule(Fact(content_maker_equipment_pc_noMic_noHeadset_budget_action='high'))
    def content_maker_equipment_pc_noMic_noheadset_high(self):
        Answer("\nMicrophone:Shure SM7B\nHeadset:Sennheiser PC 373D\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_pc_noMic_noHeadset_budget_action='low'))
    def content_maker_equipment_pc_noMic_noHeadset_budget_low(self):
        Answer("\nMicrophone:Sony ECM-CS3\nHeadset:SteelSeries Arctis 1\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_pc_mic_action='yes'))
    def content_maker_equipment_pc_mic_headset(self):
        x = test("Do You have a Headset?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_pc_mic_headset_action=x))

    @Rule(Fact(content_maker_equipment_pc_mic_headset_action='no'))
    def content_maker_equipment_pc_mic_noHeadset_budget(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_pc_mic_noHeadset_budget_action=x))

    @Rule(Fact(content_maker_equipment_pc_mic_noHeadset_budget_action='high'))
    def content_maker_equipment_pc_mic_noHeadset_budget_high(self):
        Answer("\nHeadset:Sennheiser PC 373D\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_pc_mic_noHeadset_budget_action='low'))
    def content_maker_equipment_pc_mic_noHeadset_budget_low(self):
        Answer("\nHeadset:SteelSeries Arctis 1\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_pc_mic_headset_action='yes'))
    def content_maker_equipment_pc_mic_headset_budget(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_pc_mic_headset_budget_action=x))

    @Rule(Fact(content_maker_equipment_pc_mic_headset_budget_action='high'))
    def content_maker_equipment_pc_mic_headset_budget_high(self):
        Answer("\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_pc_mic_headset_budget_action='low'))
    def content_maker_equipment_pc_mic_headset_budget_low(self):
        Answer("\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(pc_mic_action='no'))
    def content_maker_equipment(self):
        x = test("Do You have a microphone?", ['yes', 'no'])
        self.declare(Fact(pc_mic_action=x))

    @Rule(Fact(content_maker_action='no '))
    def content_maker_equipment(self):
        x = test("Do you have A Personal Computer?", ['yes', 'no'])
        self.declare(Fact(content_maker_action=x))

    # noPc

    @Rule(Fact(content_maker_pc_action='no'))
    def content_maker_equipment_noPc_mic(self):
        x = test("Do You have a microphone?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_noPc_mic_action=x))

    @Rule(Fact(content_maker_equipment_noPc_noMic_headset_action='yes'))
    def content_maker_equipment_noPc_noMic_Headset(self):
        x = test("What is your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_noPc_noMic_Headset_budget_action=x))

    @Rule(Fact(content_maker_equipment_noPc_noMic_Headset_budget_action='high'))
    def content_maker_equipment_noPc_noMic_Headset_budget_high(self):
        Answer

    @Rule(Fact(content_maker_equipment_noPc_noMic_Headset_budget_action='low'))
    def content_maker_equipment_noPc_noMic_Headset_budget_low(self):
        Answer("\nMicrophone:Sony ECM-CS3\nPC:Lenovo Y520\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_noPc_mic_action='no'))
    def content_maker_equipment_noPc_noMiccc(self):
        x = test("Do You have a Headset?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_noPc_noMic_headset_action=x))

    @Rule(Fact(content_maker_equipment_noPc_noMic_headset_action='no'))
    def content_maker_equipment_noPc_noMic_noHeadset(self):
        x = test("What is your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_noPc_noMic_noHeadset_budget_action=x))

    @Rule(Fact(content_maker_equipment_noPc_noMic_noHeadset_budget_action='high'))
    def content_maker_equipment_noPcc_noMic_noheadset_high(self):
        Answer(
            "\nPC:ROG Zephrus M16(2022)\nMicrophone:Shure SM7B\nHeadset:Sennheiser PC 373D\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_noPc_noMic_noHeadset_budget_action='low'))
    def content_maker_equipment_noPc_noMic_noHeadset_budget_low(self):
        Answer(
            "\nPC:Lenovo Y520\nMicrophone:Sony ECM-CS3\nHeadset:SteelSeries Arctis 1\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_noPc_mic_action='yes'))
    def content_maker_equipment_noPc_mic_headset(self):
        x = test("Do You have a Headset?", ['yes', 'no'])
        self.declare(Fact(content_maker_equipment_noPc_mic_headset_action=x))

    @Rule(Fact(content_maker_equipment_noPc_mic_headset_action='no'))
    def content_maker_equipment_noPc_mic_noHeadset_budget(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_noPc_mic_noHeadset_budget_action=x))

    @Rule(Fact(content_maker_equipment_noPc_mic_noHeadset_budget_action='high'))
    def content_maker_equipment_noPc_mic_noHeadset_budget_high(self):
        Answer("\nHeadset:Sennheiser PC 373D\nPC:ROG Zephrus M16(2022)\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_noPc_mic_noHeadset_budget_action='low'))
    def content_maker_equipment_noPc_mic_noHeadset_budget_low(self):
        Answer("\nHeadset:SteelSeries Arctis 1\nPC:Lenovo Y520\nRecomended Softwere:open brodcaster software")

    @Rule(Fact(content_maker_equipment_noPc_mic_headset_action='yes'))
    def content_maker_equipment_noPc_mic_headset_budget(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(content_maker_equipment_noPc_mic_headset_budget_action=x))

    @Rule(Fact(content_maker_equipment_noPc_mic_headset_budget_action='high'))
    def content_maker_equipment_noPc_mic_headset_budget_high(self):
        Answer("\nPC:ROG Zephrus M16(2022)\nRecomended Softwere:Restream")

    @Rule(Fact(content_maker_equipment_noPc_mic_headset_budget_action='low'))
    def content_maker_equipment_noPc_mic_headset_budget_low(self):
        Answer("\nPC:Lenovo Y520\nRecomended Softwere:open brodcaster software")

    # 4444444444444444444444444
    #   @Rule(Fact(Pc_mic_action ='no'))
    #  def content_maker_equipment(self):
    #     x = test("Do You have a microphone?", ['yes', 'no'])
    #    self.declare(Fact(pc_mic_action=x))

    # @Rule(Fact(content_maker_action ='no '))
    # def content_maker_equipment(self):
    #   x = test("Do you have A Personal Computer?", ['yes', 'no'])
    #  self.declare(Fact(content_maker_action=x))

    # 44444444444444444444444444444444444444444

    # personal use music production
    @Rule(Fact(action='music production'))
    def mp(self):
        x = test("Category?", ['style', 'kits'])
        self.declare(Fact(action=x))

    # personal use music production style
    @Rule(Fact(action='style'))
    def style(self):
        x = test("digital music?", ['electronic music', 'house music', 'techno'])
        self.declare(Fact(action=x))

    @Rule(Fact(action='electronic music'))
    def style_electronic_music(self):
        Answer(
            "🌎Soundtoys' Decapitator\nValhalla's VintageVerb\nXLN Audio's RC-20 Retro Color\nCableguys' VolumeShaper\nXfer Records' OTT\nFabFilter's Pro-L 2\nSpectrasonics' Omnisphere 2n\nXfer Records' Serum.")

    @Rule(Fact(action='house music'))
    def style_Hous_music(self):
        Answer(
            "Omnisphere 2 (by Spectrasonics)\nKontakt Komplete 13 (by Native Instruments)\nSerum (by Xfer Records) \nDiva (by u-He) \nPigments 3 (by Arturia)\nV Collection 8 (by Arturia)")

    @Rule(Fact(action='techno'))
    def style_Techno(self):
        Answer(
            "BABY Audio – IHNY 2. The newest addition to BABY Audio's catalog of plugins\nu-he Diva\nSonible Smart:comp 2\nArturia Pigments 2\nWide Blue Sound Elysium\niZotope Trash 2\nFabfilter Pro R\nSoundtoys Decapitator")

    # personal use music production kits
    @Rule(Fact(action='kits'))
    def kits_Budget(self):
        x = test("What is Your Budget?", ['high', 'low'])
        self.declare(Fact(action=x))

    @Rule(Fact(action='high'))
    def kits_Budget_high(self):
        Answer(
            "Headset:Bose A20 GA Headset\nSpeakers:KRK Rokits\nMidi-Keyboard:M-Audio Keystation 49 Keyboard Controller\nMicrophon:Lauten Audio Eden LT-386\nAudio Interface:M-Track 2X2 C-Series\nAcoustic Panels:t.akustik Producer Set S Professional\nRecording Software:adobe audition\nMixing Software:FL Studio")

    @Rule(Fact(action='low'))
    def kits_Budget_low(self):
        Answer(
            "Headset:Sennheiser HD 280\nSpeakers:Logitech z150\nMidi-Keyboard:Decksaver Akai MPK Mini MK2\nMicrophon:Audio-Technica AT2020\nAudio Interface:Millenium PP2B Phantom Power Supply\nAcoustic Panels:t.akustik Producer Set S Professional\nRecording Software:audacity\nMixing Software:Ableton Live.")

    #  event organizer
    @Rule(Fact(action='event organizer'))
    def event_organizer(self):
        x = test("Status of location ?", ['Indoor', 'Outdoor'])
        self.declare(Fact(event_organizer_Status_action=x))

    @Rule(Fact(event_organizer_Status_action='Outdoor'))
    def event_organizer_outdoor_Type(self):
        x = test("Type of Event ?", ['Small Party', 'Concert'])
        self.declare(Fact(event_organizer_Status_outdoor_Type_action=x))

    @Rule(Fact(event_organizer_Status_outdoor_Type_action='Small Party'))
    def event_organizer_outdoor_Type_SmallParty(self):
        Answer(
            'microphones:Schoeps Stereo-Set MK 2s\nSpeaker:Behringer B207 MP3 Active PA Speaker/Monitor\nSound Mixer:Behringer Xenyx X2222USB')

    @Rule(Fact(event_organizer_Status_outdoor_Type_action='Concert'))
    def event_organizer_outdoor_Type_Concert(self):
        Answer(
            'microphones:Schoeps Stereo-Set MK 2s\nYou should have one for each  instrument\nSpeakers:DAS Audio Vantec 6x20A/2x118A Bundle\nSpeakers Should be raised on 3 meters stand and   distributed in every other 25 meters area chunks \nSoundMixer :Mackie Profx8v2 8-Channel Compact Mixer.\nShould be tuend and wired with all the equipments\npc:mac pro m2\nSoftwere:WaveTool\nThe Stage: Stage Area Should be huge with sky covers and much higher from the surface\n ')

    @Rule(Fact(event_organizer_Status_action='Indoor'))
    def event_organizer_inDoor_Type(self):
        x = test("Type of Event ?", ['Conference'])
        self.declare(Fact(event_organizer_Status_indoor_Type_action=x))

    ## Musical Event if wanted

    @Rule(Fact(event_organizer_Status_indoor_Type_action='Conference'))
    def event_organizer_inDoor_Type_noise(self):
        x = test("Is there any noise cancellation in the location ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_Status_indoor_Type_noise_action=x))

    #### Start Of Noise cancellation:Yes
    @Rule(Fact(event_organizer_Status_indoor_Type_noise_action='Yes'))
    def event_organizer_inDoor_Type_noise_pc(self):
        x = test("Do You Have A Personal Computer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_Status_indoor_Type_noise_pc_action=x))

    #### Start Of Noise cancellation PC:Yes
    @Rule(Fact(event_organizer_Status_indoor_Type_noise_pc_action='Yes'))
    def event_organizer_inDoor_Type_noise_pc_mic(self):
        x = test("Do You have a microphone for each one who's going to paticipate ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_indoor_Type_noise_pc_mic_action=x))

    @Rule(Fact(event_organizer_indoor_Type_noise_pc_mic_action='Yes'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker='Yes'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker_mixer_Ans(self):
        Answer(
            'microphones: You should have one for each participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool\n')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget_low_Ans(self):
        Answer(
            'microphones: You should have one for each  participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer: Studiomaster Mini 6U\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\n ')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_pc_mic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer: SoundCraft Ui24R\n  Should be tuend and wired with all the equipment\nSoftwere:WaveTool\n')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_speaker='No'))
    def event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  participant\n Speakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\n')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_pc_mic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_indoor_Type_noise_pc_mic_action='No'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker='Yes'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker_mixer_Ans(self):
        Answer('microphones:Sennheiser e935\nYou should have one for each  participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones:Sennheiser e935\nYou should have one for each  participant\n Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_pc_noMic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones:Sennheiser e935\nYou should have one for each  participant\n Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Studiomaster Mini 6U\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_speaker='No'))
    def event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_mixer_Ans(self):
        Answer('microphones:Shure SM58\nYou should have one for each  participant\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones:Shure SM58\nYou should have one for each participant\nSpeakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_pc_noMic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones:Sennheiser e935\nYou should have one for each participant\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\n')

    ##No pc
    @Rule(Fact(event_organizer_Status_indoor_Type_noise_pc_action='No'))
    def event_organizer_inDoor_Type_noise_noPc_mic(self):
        x = test("Do You have a microphone for each one who's going to paticipate ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_conf_noise_noPc_mic_action=x))
#
    @Rule(Fact(event_organizer_inDoor_conf_noise_noPc_mic_action='Yes'))
    def e22(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker=x))
 
    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker='Yes'))
    def even333r(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_noPc_mic_speaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')
    
    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Studiomaster Mini 6U\nShould be tuend and wired with all the equipment\npc:mac pro 2017\n Softwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_noPc_mic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_speaker='No'))
    def event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  participant\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro 2017\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_noPc_mic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_conf_noise_noPc_mic_action='No'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker=x))
 
    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker='Yes'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  participant\n Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Studiomaster Mini 6U\n Should be tuend and wired with all the equipment\npc:mac pro 2017\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_speaker='No'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_mixer_Ans(self):
         Answer('microphones: You should have one for each  participant\n Speakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  participant Speakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro 2019\nSoftwere:WaveTool')
   
    @Rule(Fact(event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noise_noPc_noMic_noSpeaker_Nomixer_Budget_high_Ans(self):
         Answer('microphones: You should have one for each  participant Speakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')  
 
    @Rule(Fact(event_organizer_Status_indoor_Type_noise_action='No'))
    def event_organizer_inDoor_Type_noNoise_pc(self):
        x = test("Do You Have A Personal Computer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_Status_indoor_Type_noNoise_pc_action=x))


# No noise


    #### Start Of Noise cancellation PC:Yes
    @Rule(Fact(event_organizer_Status_indoor_Type_noNoise_pc_action='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_mic(self):
        x = test("Do You have a microphone for each one who's going to paticipate ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_indoor_Type_noNoise_pc_mic_action=x))

    @Rule(Fact(event_organizer_indoor_Type_noNoise_pc_mic_action='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  instrumentSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Studiomaster Mini 6U\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\n SoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad\n')
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_speaker='No'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_mixer_Ans(self):
         Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
    def event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  instrument\n Speakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')    

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_pc_mic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
    @Rule(Fact(event_organizer_indoor_Type_noNoise_pc_mic_action='No'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_mixer_Ans(self):
        Answer('microphones:DPA 4099 core\nYou should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones:DPA 4099 core\nYou should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Studiomaster Mini 6U Should be tuend and wired with all the equipmentSoftwere:WaveToolSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones:DPA 4099 core\nYou should have one for each  instrument Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_speaker='No'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_mixer_Ans(self):
      Answer('microphones:DPA 4099 Core\nYou should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling \n SoundMixer :Should be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
    
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget_low_Ans(self):
         Answer('microphones:DPA 4099 Core\nYou should have one for each  instrument\nSpeakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
    
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_pc_noMic_noSpeaker_Nomixer_Budget_high_Ans(self):
      Answer('microphones:DPA 4099 Core\nYou should have one for each  instrumentSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveToolSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')
    ##No pc
    @Rule(Fact(event_organizer_Status_indoor_Type_noNoise_pc_action='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic(self):
        x = test("Do You have a microphone for each one who's going to paticipate ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_conf_noNoise_noPc_mic_action=x))
#
    @Rule(Fact(event_organizer_inDoor_conf_noNoise_noPc_mic_action='Yes'))
    def e22(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker=x))
 
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker='Yes'))
    def even333r(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_mixer_Ans(self):
        Answer('microphones: You should have one for each instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool')     
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :Studiomaster Mini 6U\nShould be tuend and wired with all the equipment\npc:mac pro 2017\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers: Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer: SoundCraft Ui24R\nShould be tuend and wired with all the equipment\nSoftwere:WaveTool\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_speaker='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n SoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:2017\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
   
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_noPc_mic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
    @Rule(Fact(event_organizer_inDoor_conf_noNoise_noPc_mic_action='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker(self):
        x = test("Do you have Speakers ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker=x))
 
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker='Yes'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_mixer_Ans(self):
         Answer('microphones: You should have one for each  instrument\nSpeakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling \nSoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget_low_Ans(self):
         Answer('microphones: You should have one for each instrument Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Studiomaster Mini 6U \nShould be tuend and wired with all the equipment\npc:mac pro 2019\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
    
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument Speakers:Speakers Should be distributed in every corner and tiwce the count on the ceiling\n  SoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_speaker='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_mixer(self):
        x = test("Do you have a sound Mixer ?", ['Yes', 'No'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_mixer=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_mixer='Yes'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_mixer_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :Should be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad') 
    
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_mixer='No'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget(self):
        x = test("What is Your Budget ?", ['High', 'Low'])
        self.declare(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget=x))

    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget='Low'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget_low_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:Behringer Eurolive B112D\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling  \nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro 2019\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')    
    
    @Rule(Fact(event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget='High'))
    def event_organizer_inDoor_Type_noNoise_noPc_noMic_noSpeaker_Nomixer_Budget_high_Ans(self):
        Answer('microphones: You should have one for each  instrument\nSpeakers:JBL SRX835P - 15\nSpeakers Should be distributed in every corner and tiwce the count on the ceiling\nSoundMixer :SoundCraft Ui24R\nShould be tuend and wired with all the equipment\npc:mac pro m2\nSoftwere:WaveTool\nSoundProof:a quarter of the wall area should be covered with accustic panels the ground has to be coverd with thick rug pad')  




engine = Sound_Kit_Aid()
engine.reset()
engine.run()
