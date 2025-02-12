import operations
from Application import *
from CONST import *

def newaccount_contents(frame):
    global img2, imglabel2
    img2 = logo(width=200, height=100, file='logo.png', resize=True)
    #imglabel2 = Label(frame, image=img2, bd=0, bg=color_bg)
    #imglabel2.place(x=10, y=30)
    topbar_contents = {'< Back': frame.destroy, 'Help':''}
    topbar(frame, topbar_contents)

    def pincode_event(e):
        pin = pincode.get()
        global found
        csv_file = csv.reader(open('india.csv', "r"), delimiter=",")
        for row in csv_file:
            if pin == row[0]:
                district.config(state=NORMAL)
                state.config(state=NORMAL)
                district.delete(0, END)
                state.delete(0, END)
                district.insert(0, row[1].title())
                state.insert(0, row[2].title())
                district.config(state=DISABLED)
                state.config(state=DISABLED)
                found = True
                break
            else:
                found = False
        if not found:
            district.config(state=NORMAL)
            state.config(state=NORMAL)
            district.delete(0, END)
            state.delete(0, END)
            district.config(state=DISABLED)
            state.config(state=DISABLED)

    global filename

    def file():
        global filename
        filename = filedialog.askopenfile(initialdir="/", title='Select a file', filetypes=(('All files', '*.*'),
                                                                                            ('PDF files', '*.pdf'),
                                                                                            ('JPG files', '*.jpg'),
                                                                                            ('JPEG files', '*.jpeg')))
        try:
            filename = filename.name
        except:
            pass

    X_REF = 80
    X_REF2 = 600
    Y_REF = 170
    font = ("Lato", 10)

    global gender, accounttype
    accounttype = StringVar()
    accounttype.set('Savings')
    gender = StringVar()
    gender.set('None')
    ######LABELS
    l_title = Label(frame, text='Title', font=font, bg=color_bg, anchor='w', fg='grey')
    l_firstname = Label(frame, text='First name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_lastname = Label(frame, text='Last name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_dob = Label(frame, text='DOB (DD/MM/YYYY)', font=font, bg=color_bg, anchor='w', fg='grey')
    l_acctype = Label(frame, text='Account type', font=font, bg=color_bg, anchor='w', fg='grey', )
    l_mobile = Label(frame, text='Mobile number', font=font, bg=color_bg, anchor='w', fg='grey')
    l_email = Label(frame, text='Email', font=font, bg=color_bg, anchor='w', fg='grey')
    l_gender = Label(frame, text='Gender', font=font, bg=color_bg, anchor='w', fg='grey')
    l_nationality = Label(frame, text='Nationality', font=font, bg=color_bg, anchor='w', fg='grey')
    l_address = Label(frame, text='Address', font=font, bg=color_bg, anchor='w', fg='grey')
    l_pincode = Label(frame, text='Pincode', font=font, bg=color_bg, anchor='w', fg='grey')
    l_district = Label(frame, text='District', font=font, bg=color_bg, anchor='w', fg='grey')
    l_state = Label(frame, text='State', font=font, bg=color_bg, anchor='w', fg='grey')
    l_kyc = Label(frame, text='KYC Document', font=font, bg=color_bg, anchor='w', fg='grey')
    l_refno = Label(frame, text='Reference No.', font=font, bg=color_bg, anchor='w', fg='grey')

    l_title_n = Label(frame, text='Title', font=font, bg=color_bg, anchor='w', fg='grey')
    l_firstname_n = Label(frame, text='Nominee First name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_lastname_n = Label(frame, text='Nominee Last name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_mobile_n = Label(frame, text='Nominee Mobile number', font=font, bg=color_bg, anchor='w', fg='grey')
    l_email_n = Label(frame, text='Nominee Email', font=font, bg=color_bg, anchor='w', fg='grey')
    l_relationship_n = Label(frame, text='Relationship', font=font, bg=color_bg, anchor='w', fg='grey')

    ######LABELS PLACE
    l_title.place(x=X_REF, y=Y_REF, width=100, height=25)
    l_firstname.place(x=X_REF + 90, y=Y_REF, width=100, height=25)
    l_lastname.place(x=X_REF + 260, y=Y_REF, width=100, height=25)
    l_dob.place(x=X_REF, y=Y_REF + 60, width=150, height=25)
    l_acctype.place(x=X_REF + 220, y=Y_REF + 60, width=150, height=25)
    l_mobile.place(x=X_REF, y=Y_REF + 120, width=150, height=25)
    l_email.place(x=X_REF + 220, y=Y_REF + 120, width=100, height=25)
    l_gender.place(x=X_REF, y=Y_REF + 180, width=150, height=25)
    l_nationality.place(x=X_REF + 220, y=Y_REF + 180, width=100, height=25)
    l_address.place(x=X_REF, y=Y_REF + 240, width=100, height=25)
    l_pincode.place(x=X_REF, y=Y_REF + 300, width=100, height=25)
    l_district.place(x=X_REF + 110, y=Y_REF + 300, width=100, height=25)
    l_state.place(x=X_REF + 270, y=Y_REF + 300, width=100, height=25)
    l_kyc.place(x=X_REF, y=Y_REF + 360, width=100, height=25)
    l_refno.place(x=X_REF + 240, y=Y_REF + 360, width=180, height=25)

    l_title_n.place(x=X_REF2, y=Y_REF, width=100, height=25)
    l_firstname_n.place(x=X_REF2 + 90, y=Y_REF, width=120, height=25)
    l_lastname_n.place(x=X_REF2 + 260, y=Y_REF, width=120, height=25)
    l_mobile_n.place(x=X_REF2, y=Y_REF + 60, width=150, height=25)
    l_email_n.place(x=X_REF2 + 220, y=Y_REF + 60, width=100, height=25)
    l_relationship_n.place(x=X_REF2, y=Y_REF + 120, width=100, height=25)

    ######ENTRIES
    title = Combobox(frame, state="readonly", font=font)
    title['values'] = (' Mr', ' Mrs', ' Miss', ' Ms')
    title["background"] = '#ff0000'
    firstname = Entry(frame, bd=1, relief=SOLID, font=font)
    lastname = Entry(frame, bd=1, relief=SOLID, font=font)
    dob = Entry(frame, bd=1, relief=SOLID, font=font)
    acctype1 = Radiobutton(frame, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings',
                           activebackground=color_bg, anchor='w')
    acctype2 = Radiobutton(frame, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current',
                           activebackground=color_bg)
    mobile = Entry(frame, bd=1, relief=SOLID, font=font)
    email = Entry(frame, bd=1, relief=SOLID, font=font)
    gender1 = Radiobutton(frame, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                          activebackground=color_bg, anchor='w')
    gender2 = Radiobutton(frame, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                          activebackground=color_bg)
    nation = Combobox(frame, width=27, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka')
    nation["background"] = '#ff0000'
    address = Entry(frame, bd=1, relief=SOLID, font=font)
    pincode = Entry(frame, bd=1, relief=SOLID, font=font)
    pincode.bind("<FocusOut>", pincode_event)
    district = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                     disabledforeground="black")
    state = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    kyc_combo = Combobox(frame, width=27, state="readonly", font=font)
    kyc_combo['values'] = (' PAN Card', ' Aadhaar Card', ' Passport')
    kyc_combo["background"] = '#ff0000'
    refno = Entry(frame, bd=1, relief=SOLID, font=font, disabledbackground="white", disabledforeground="black")

    title_n = Combobox(frame, state="readonly", font=font)
    title_n['values'] = (' Mr', ' Mrs', ' Miss', ' Ms')
    title_n["background"] = '#ff0000'
    firstname_n = Entry(frame, bd=1, relief=SOLID, font=font)
    lastname_n = Entry(frame, bd=1, relief=SOLID, font=font)
    mobile_n = Entry(frame, bd=1, relief=SOLID, font=font)
    email_n = Entry(frame, bd=1, relief=SOLID, font=font)
    relationship = Combobox(frame, state="readonly", font=font)
    relationship['values'] = (' Father', ' Mother', ' Friend', ' Family')
    relationship["background"] = '#ff0000'

    ######ENTRIES PLACE
    title.place(x=X_REF, y=Y_REF + 25, height=23, width=70)
    firstname.place(x=X_REF + 90, y=Y_REF + 25, width=150, height=23)
    lastname.place(x=X_REF + 90 + 170, y=Y_REF + 25, width=150, height=23)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=150, height=23)
    acctype1.place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25)
    acctype2.place(x=X_REF + 320, y=Y_REF + 60 + 25, width=100, height=25)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=23)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=23)
    gender1.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25)
    gender2.place(x=X_REF + 100, y=Y_REF + 180 + 25, width=100, height=25)
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=23)
    address.place(x=X_REF, y=Y_REF + 240 + 25, width=420, height=23)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=23)
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=23)
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=23)
    kyc_combo.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=23)
    refno.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=23)
    upload = Button(frame, text='Upload', bd=1, relief=SOLID, command=file, cursor='hand2')
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=23)

    title_n.place(x=X_REF2, y=Y_REF + 25, height=23, width=70)
    firstname_n.place(x=X_REF2 + 90, y=Y_REF + 25, width=150, height=23)
    lastname_n.place(x=X_REF2 + 90 + 170, y=Y_REF + 25, width=150, height=23)
    mobile_n.place(x=X_REF2, y=Y_REF + 60 + 25, width=200, height=23)
    email_n.place(x=X_REF2 + 220, y=Y_REF + 60 + 25, width=200, height=23)
    relationship.place(x=X_REF2, y=Y_REF + 25 + 120, height=23, width=100)

    l_captcha_n = Label(frame, text='Enter the shown text', font=font, bg=color_bg, anchor='w', fg='grey')
    l_captcha_n.place(x=X_REF2 + 149, y=Y_REF + 180, width=145, height=25)

    global bg_display, bg_img
    bg_img = logo(300, height=300, file='background.png', resize=False)

    bg_display = Label(frame, image=bg_img, bg=color_bg, bd=0, relief=SOLID, )
    bg_display.place(x=X_REF2, y=Y_REF + 205, width=150, height=30)

    captcha_display = Label(frame, text='', font=('times', 20), bg='#CBCBCB', bd=0, relief=SOLID, )
    captcha_display.place(x=X_REF2 + 40, y=Y_REF + 205, width=70, height=30)

    captcha_entry = Entry(frame, bg=color_bg, bd=1, relief=SOLID, font=('times', 20), justify=CENTER)
    captcha_entry.place(x=X_REF2 + 149, y=Y_REF + 205, width=150, height=30)

    captcha_refresh = Button(frame, text='↻', bd=0, relief=SOLID,
                             command=lambda: change_captcha(captcha_display, captcha_entry), font=('times', 15),
                             bg=color_bg, activebackground=color_bg, fg='red')
    captcha_refresh.place(x=X_REF2 + 301, y=Y_REF + 205, width=20, height=20)

    change_captcha(captcha_display, captcha_entry)

    l_otp_n = Label(frame, text='One time password', font=font, bg=color_bg, anchor='w', fg='grey')
    l_otp_n.place(x=X_REF2, y=Y_REF + 250, width=145, height=25)

    otp_entry = Entry(frame, bg=color_bg, bd=1, relief=SOLID, font=('times', 20), justify=CENTER)
    otp_entry.place(x=X_REF2, y=Y_REF + 275, width=150, height=30)

    def otp_button():
        if check_captcha(captcha_entry.get()):
            if check_email(email.get()):
                otp_entry.delete(0, END)
                global otp
                otp = str(random.randint(1111, 9999))
                Thread(target=lambda: send_otp(email.get(), otp)).start()
                otp_sent_label.config(text='Check your email for the OTP')
                otp_resend.place(x=X_REF2 + 151, y=Y_REF + 275, width=20, height=20)
                timerthread = Thread(target=timer)
                timerthread.start()
                otp_send.destroy()
            else:
                l_email.config(fg='red')
                notification_label.config(text='Invalid Email')
        else:
            notification_label.config(text='Invalid Captcha')

    session_expired = False
    def timer():
        global session_expired
        try:
            otp_resend.config(state=DISABLED)
            for i in reversed(range(120)):
                timer_label.config(text=f'Resend OTP in {i} seconds.')
                sleep(1)
                timer_label.update()
                if session_expired:
                    break

            timer_label.config(text='')
            otp_resend.config(state=NORMAL)
        except:
            pass

    otp_send = Button(frame, text='Send OTP', bd=1, relief=SOLID, font=('lato', 11), bg=color_bg, command=otp_button,
                      activebackground=color_bg, cursor='hand2')
    otp_send.place(x=X_REF2, y=Y_REF + 275, width=150, height=30)

    otp_resend = Button(frame, text='↻', bd=0, relief=SOLID, font=('times', 15), bg=color_bg, activebackground=color_bg,
                        fg='red', command=otp_button)
    otp_sent_label = Label(frame, text='', bg=color_bg, fg='green')
    otp_sent_label.place(x=X_REF2 + 171, y=Y_REF + 270, width=200, height=20)
    timer_label = Label(frame, text='', bg=color_bg, fg='red')
    timer_label.place(x=X_REF2 + 171, y=Y_REF + 290, width=200, height=20)

    varagree = IntVar()

    def agree():
        if varagree.get() == 1:
            button_signup.config(state=NORMAL, cursor='hand2')
        else:
            button_signup.config(state=DISABLED, cursor='exchange')

    agree_termsandconditions = Checkbutton(frame, text="I agree to the terms and conditions", height=5, width=20,
                                           bg=color_bg, activebackground=color_bg, command=agree, variable=varagree)
    agree_termsandconditions.place(x=X_REF2, y=Y_REF + 325, width=200, height=20)

    check_list_empties = {title: l_title, firstname: l_firstname, lastname: l_lastname, dob: l_dob,
                          mobile: l_mobile, email: l_email, nation: l_nationality, address: l_address,
                          pincode: l_pincode, state: l_pincode, kyc_combo: l_kyc,
                          refno: l_refno, title_n: l_title_n, firstname_n: l_firstname_n, lastname_n: l_lastname_n,
                          mobile_n: l_mobile_n, email_n: l_email_n, relationship: l_relationship_n}

    def signup():
        global all_checked
        all_checked = False
        for item in check_list_empties.keys():
            if item.get() == '':
                check_list_empties[item].config(fg='red')
                all_checked = False
                notification_label.config(text='Invalid Entry')
                break
            else:
                all_checked = True
        if all_checked:
            if check_dob(dob.get()) is True:
                if check_mobilenumber(mobile.get()) is True:
                    if check_email(email.get()) is True:
                        if gender.get() != "None":
                            if check_captcha(captcha_entry.get()):
                                if check_mobilenumber(mobile_n.get()):
                                    if check_email(email_n.get()):
                                        if otp == str(otp_entry.get()):
                                            operations.signup(
                                                title.get(), firstname.get(), lastname.get(), dob.get(),
                                                accounttype.get(),
                                                mobile.get(), email.get(),
                                                gender.get(), nation.get(), address.get(), pincode.get(),
                                                district.get(),
                                                state.get(), kyc_combo.get(), refno.get(),
                                                filename, title_n.get(), firstname_n.get(), lastname_n.get(),
                                                mobile_n.get(), email_n.get(), relationship.get()
                                            )
                                            while True:
                                                if operations.upload_success:
                                                    clear_all_entries()
                                                    break
                                                else:
                                                    pass
                                        else:
                                            otp_sent_label.config(text='Incorrect OTP, Try again')
                                    else:
                                        l_email_n.config(fg='red')
                                        notification_label.config(text='Invalid Email')
                                else:
                                    l_mobile_n.config(fg='red')
                                    notification_label.config(text='Invalid Email')
                            elif captcha_entry.get() == '':
                                pass
                            else:
                                change_captcha(captcha_display, captcha_entry)
                        else:
                            l_gender.config('red')
                            notification_label.config(text='Invalid Email')
                    else:
                        l_email.config(fg='red')
                        notification_label.config(text='Invalid Email')
                else:
                    l_mobile.config(fg='red')
                    notification_label.config(text='Invalid Email')
            else:
                l_dob.config(fg='red')
                notification_label.config(text='Invalid Email')
        else:
            print('NOT ALL CHECKED')

    def all_back_to_grey(e):
        for item in check_list_empties.values():
            item.config(fg='grey')
        notification_label.config(text='')

    def clear_all_entries():
        title.set("")
        firstname.delete(0,END)
        lastname.delete(0,END)
        dob.delete(0,END)
        accounttype.set('Savings')
        mobile.delete(0,END)
        email.delete(0,END)
        gender.set('None')
        #nation.set('None')
        nation.set('')
        address.delete(0,END)
        pincode.delete(0,END)
        district.config(state=NORMAL)
        district.delete(0,END)
        district.config(state=NORMAL)
        state.config(state=NORMAL)
        state.delete(0,END)
        state.config(state=NORMAL)
        kyc_combo.set('')
        refno.delete(0,END)
        title_n.set("")
        firstname_n.delete(0,END)
        lastname_n.delete(0,END)
        mobile_n.delete(0,END)
        email_n.delete(0,END)
        relationship.set("")
        change_captcha(captcha_display, captcha_entry)
        otp_entry.delete(0,END)
        otp_send = Button(frame, text='Send OTP', bd=1, relief=SOLID, font=('lato', 11), bg=color_bg,command=otp_button,activebackground=color_bg, cursor='hand2')
        otp_send.place(x=X_REF2, y=Y_REF + 275, width=150, height=30)
        otp_resend.place(x=X_REF2 + 151, y=Y_REF + 275+150, width=20, height=20)
        otp_sent_label.config(text='')
        global session_expired
        session_expired = True



    for item in check_list_empties.keys():
        item.bind("<FocusIn>", all_back_to_grey)
    captcha_entry.bind("<FocusIn>", all_back_to_grey)
    captcha_entry.bind("<Key>", all_back_to_grey)

    button_signup = Button(frame, bd=0, text='Sign up', bg='#B3E982', fg='#283556', activebackground='#BCEC91',
                           activeforeground='#283556', font=("Lato", 10, 'bold'), cursor='hand2', command=signup)
    button_signup.place(x=(w - X_REF2 / 2) - 250 / 2, y=Y_REF + 360 + 21, width=250, height=27)
    button_signup.config(state=DISABLED, cursor='exchange')

    notification_label = Label(frame, text='', bg=color_bg, fg='red', anchor='e', font=('lato', 12))
    notification_label.place(x=w - 210, y=35, width=200, height=30)
