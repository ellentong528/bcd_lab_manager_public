# bcd_lab_participant_workflow.py
# Run with: streamlit run bcd_lab_participant_workflow.py

import streamlit as st

st.set_page_config(
    page_title="BCD Lab Participant Workflow",
    page_icon="🧠",
    layout="wide",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.app-title {
    text-align: center;
    font-size: 44px;
    font-weight: 850;
    margin-bottom: 0.2rem;
}

.app-subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
    margin-bottom: 2rem;
}

.card {
    background: white;
    border: 1px solid #e8e8e8;
    border-radius: 18px;
    padding: 22px 26px;
    margin-bottom: 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}

.card h3 {
    margin-top: 0;
    margin-bottom: 10px;
}

.phone { border-left: 8px solid #2563eb; }
.email { border-left: 8px solid #7c3aed; }
.schedule { border-left: 8px solid #16a34a; }
.warning { border-left: 8px solid #f59e0b; }
.stop { border-left: 8px solid #dc2626; }
.neutral { border-left: 8px solid #64748b; }

.step-label {
    display: inline-block;
    background: #f1f5f9;
    color: #0f172a;
    border-radius: 999px;
    padding: 5px 11px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.pill {
    display: inline-block;
    border-radius: 999px;
    padding: 6px 12px;
    margin-right: 6px;
    margin-bottom: 8px;
    background: #eef2ff;
    font-weight: 700;
    font-size: 13px;
}

.checklist li {
    margin-bottom: 8px;
}

.small {
    color: #666;
    font-size: 14px;
}

div.stButton > button {
    border-radius: 14px;
    height: 3rem;
    font-weight: 700;
}
</style>
""",
    unsafe_allow_html=True,
)


# -----------------------------
# Helper functions
# -----------------------------
def card(title: str, body: str, style: str = "neutral") -> None:
    st.markdown(
        f"""
<div class="card {style}">
    <h3>{title}</h3>
    <div>{body}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def checklist(items):
    for item in items:
        st.checkbox(item, key=f"{item}_{hash(item)}")


def reset():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="app-title">BCD Lab Participant Workflow</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Interactive SOP for participant contact, scheduling, reminders, database updates, and calendar updates.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Quick Rules")
    st.markdown(
        """
**Respect preference**  
If a family prefers email, use email only. Do not call or text.

**Voicemail rule**  
Only leave a voicemail during the first phone outreach.

**Regular follow-up timing**  
Wait **3–7 days** between contact attempts.

**After contact #5**  
Wait **3 days**, then send the next-month outreach.

**Calendly appointments**  
Calendly sends confirmation and reminder emails automatically. RAs should not send those manually.
        """
    )
    st.divider()
    if st.button("Reset all checkboxes / selections"):
        reset()

# -----------------------------
# Tabs
# -----------------------------
contact_tab, scheduling_tab, quick_reference_tab = st.tabs(
    ["1. Contact Workflow", "2. Scheduling & Reminders", "Quick Reference"]
)

# -----------------------------
# Contact Workflow Tab
# -----------------------------
with contact_tab:
    st.header("Contact Workflow")
    st.write("Use this section when you are trying to reach a family.")

    col_main, col_tasks = st.columns([2, 1])

    with col_main:
        contact_preference = st.radio(
            "Step 1. What is the family's preferred contact method?",
            ["No preference / Prefers calls", "Prefers email"],
            horizontal=True,
        )

        st.divider()

        if contact_preference == "No preference / Prefers calls":
            card(
                "Phone / No Preference Path",
                """
                Use this path when the family has no listed contact preference or prefers calls.
                <br><br>
                <span class="pill">Call</span>
                <span class="pill">Email</span>
                <span class="pill">Text</span>
                """,
                "phone",
            )

            stage = st.radio(
                "Step 2. Which stage are you in?",
                [
                    "Contact Attempt #1",
                    "Contact Attempts #2–#5",
                    "After Contact Attempt #5",
                    "Family has responded",
                ],
            )

            if stage == "Contact Attempt #1":
                answered = st.radio(
                    "Did the family answer the first call?",
                    ["I am about to call", "Yes", "No"],
                    horizontal=True,
                )

                if answered == "I am about to call":
                    card(
                        "Do this now",
                        """
                        <ul class="checklist">
                            <li>Call the family using the project-specific BCDLab calling script.</li>
                            <li>Make sure you are using the correct script for the study/project.</li>
                        </ul>
                        """,
                        "phone",
                    )
                    todays_tasks = [
                        "Call the family using the project-specific script",
                    ]
                    next_step = "If they answer, follow the study-specific script. If they do not answer, leave a voicemail, send the first-contact email, and send the first-contact text."

                elif answered == "Yes":
                    card(
                        "Family answered",
                        """
                        <ul class="checklist">
                            <li>Follow the study-specific script.</li>
                            <li>If the family schedules an appointment, go to the Scheduling & Reminders tab.</li>
                        </ul>
                        """,
                        "schedule",
                    )
                    todays_tasks = [
                        "Follow the study-specific script",
                        "If scheduled, complete the Scheduling & Reminders workflow",
                    ]
                    next_step = "Move to Scheduling & Reminders if the family schedules."

                else:
                    card(
                        "No answer during Contact Attempt #1",
                        """
                        Complete all three:
                        <ul class="checklist">
                            <li>Leave a voicemail.</li>
                            <li>Send the First Contact Email Template.</li>
                            <li>Send the First Contact Text Template.</li>
                        </ul>
                        <p><b>Then:</b> Wait 3–7 days before Contact Attempt #2.</p>
                        """,
                        "warning",
                    )
                    todays_tasks = [
                        "Leave a voicemail",
                        "Send the First Contact Email Template",
                        "Send the First Contact Text Template",
                    ]
                    next_step = "Wait 3–7 days before Contact Attempt #2."

            elif stage == "Contact Attempts #2–#5":
                contact_attempt = st.selectbox(
                    "Which contact attempt are you making today?",
                    ["#2", "#3", "#4", "#5"],
                )

                card(
                    f"Contact Attempt {contact_attempt}",
                    """
                    Only do this if 3–7 days have passed since the previous contact attempt.
                    <br><br>
                    Complete all three:
                    <ul class="checklist">
                        <li>Call the family.</li>
                        <li><b>Do not leave another voicemail.</b></li>
                        <li>Send the Follow-up Email Template.</li>
                        <li>Send the Follow-up Text Template.</li>
                    </ul>
                    """,
                    "phone",
                )

                todays_tasks = [
                    "Call the family",
                    "Do not leave another voicemail",
                    "Send the Follow-up Email Template",
                    "Send the Follow-up Text Template",
                ]

                if contact_attempt == "#5":
                    card(
                        "If there is still no response after Contact Attempt #5",
                        """
                        <ul class="checklist">
                            <li>Wait 3 days.</li>
                            <li>Send the Next-Month Follow-up Email Template.</li>
                            <li>Send the Next-Month Follow-up Text Template.</li>
                            <li>Pause recruitment afterward unless instructed otherwise.</li>
                        </ul>
                        """,
                        "warning",
                    )
                    next_step = "If there is still no response, wait 3 days, then send the next-month email and text."
                else:
                    next_num = int(contact_attempt.replace("#", "")) + 1
                    next_step = f"If there is still no response, wait 3–7 days before Contact Attempt #{next_num}."

            elif stage == "After Contact Attempt #5":
                card(
                    "After Contact Attempt #5",
                    """
                    Use this only if the family still has not responded after the fifth contact.
                    <br><br>
                    <span class="step-label">Wait 3 days after Contact Attempt #5</span>
                    <ul class="checklist">
                        <li>Send the Next-Month Follow-up Email Template.</li>
                        <li>Send the Next-Month Follow-up Text Template.</li>
                        <li>Pause recruitment afterward unless instructed otherwise.</li>
                    </ul>
                    """,
                    "stop",
                )
                todays_tasks = [
                    "Confirm 3 days have passed since Contact Attempt #5",
                    "Send the Next-Month Follow-up Email Template",
                    "Send the Next-Month Follow-up Text Template",
                    "Pause recruitment afterward unless instructed otherwise",
                ]
                next_step = "Pause recruitment unless instructed otherwise."

            else:
                card(
                    "Family responded",
                    """
                    <ul class="checklist">
                        <li>Follow the study-specific script.</li>
                        <li>If the family schedules, go to the Scheduling & Reminders tab.</li>
                    </ul>
                    """,
                    "schedule",
                )
                todays_tasks = [
                    "Follow the study-specific script",
                    "If scheduled, complete the Scheduling & Reminders workflow",
                ]
                next_step = "Move to Scheduling & Reminders if the family schedules."

        else:
            card(
                "Email-Only Path",
                """
                Use this path when the family prefers email.
                <br><br>
                <b>Important:</b> Do not call or text the family unless they later ask to be contacted another way.
                <br><br>
                <span class="pill">Email only</span>
                """,
                "email",
            )

            stage = st.radio(
                "Step 2. Which stage are you in?",
                [
                    "Contact Attempt #1",
                    "Contact Attempts #2–#5",
                    "After Contact Attempt #5",
                    "Family has responded",
                ],
            )

            if stage == "Contact Attempt #1":
                card(
                    "Contact Attempt #1: Email only",
                    """
                    <ul class="checklist">
                        <li>Send the First Contact Email Template.</li>
                        <li>Include the experiment-specific Calendly link.</li>
                    </ul>
                    <p><b>Then:</b> Wait 3–7 days before Contact Attempt #2.</p>
                    """,
                    "email",
                )
                todays_tasks = [
                    "Send the First Contact Email Template",
                    "Include the experiment-specific Calendly link",
                ]
                next_step = "Wait 3–7 days before Contact Attempt #2."

            elif stage == "Contact Attempts #2–#5":
                contact_attempt = st.selectbox(
                    "Which email contact attempt are you sending today?",
                    ["#2", "#3", "#4", "#5"],
                )

                card(
                    f"Email Contact Attempt {contact_attempt}",
                    """
                    Only do this if 3–7 days have passed since the previous email.
                    <br><br>
                    <ul class="checklist">
                        <li>Send the Follow-up Email Template.</li>
                        <li>Do not call.</li>
                        <li>Do not text.</li>
                    </ul>
                    """,
                    "email",
                )

                todays_tasks = [
                    "Send the Follow-up Email Template",
                    "Do not call",
                    "Do not text",
                ]

                if contact_attempt == "#5":
                    card(
                        "If there is still no response after Contact Attempt #5",
                        """
                        <ul class="checklist">
                            <li>Wait 3 days.</li>
                            <li>Send the Next-Month Follow-up Email Template.</li>
                            <li>Pause recruitment afterward unless instructed otherwise.</li>
                        </ul>
                        """,
                        "warning",
                    )
                    next_step = "If there is still no response, wait 3 days, then send the next-month email."
                else:
                    next_num = int(contact_attempt.replace("#", "")) + 1
                    next_step = f"If there is still no response, wait 3–7 days before Contact Attempt #{next_num}."

            elif stage == "After Contact Attempt #5":
                card(
                    "After Contact Attempt #5",
                    """
                    Use this only if the family still has not responded after the fifth email contact.
                    <br><br>
                    <span class="step-label">Wait 3 days after Contact Attempt #5</span>
                    <ul class="checklist">
                        <li>Send the Next-Month Follow-up Email Template.</li>
                        <li>Do not call.</li>
                        <li>Do not text.</li>
                        <li>Pause recruitment afterward unless instructed otherwise.</li>
                    </ul>
                    """,
                    "stop",
                )
                todays_tasks = [
                    "Confirm 3 days have passed since Contact Attempt #5",
                    "Send the Next-Month Follow-up Email Template",
                    "Do not call",
                    "Do not text",
                    "Pause recruitment afterward unless instructed otherwise",
                ]
                next_step = "Pause recruitment unless instructed otherwise."

            else:
                card(
                    "Family responded",
                    """
                    <ul class="checklist">
                        <li>Reply by email unless they ask for another contact method.</li>
                        <li>Follow the study-specific script.</li>
                        <li>If the family schedules, go to the Scheduling & Reminders tab.</li>
                    </ul>
                    """,
                    "schedule",
                )
                todays_tasks = [
                    "Reply by email unless they ask for another contact method",
                    "Follow the study-specific script",
                    "If scheduled, complete the Scheduling & Reminders workflow",
                ]
                next_step = "Move to Scheduling & Reminders if the family schedules."

    with col_tasks:
        card(
            "Today’s Task List",
            "<p class='small'>Based on your selections, complete the checklist below.</p>",
            "neutral",
        )
        checklist(todays_tasks)
        st.info(next_step)

# -----------------------------
# Scheduling & Reminders Tab
# -----------------------------
with scheduling_tab:
    st.header("Scheduling & Reminders")
    st.write("Use this section once a family has scheduled or is actively scheduling an appointment.")

    sched_col, task_col = st.columns([2, 1])

    with sched_col:
        scheduling_method = st.radio(
            "How was the appointment scheduled?",
            [
                "Scheduled through Calendly",
                "Scheduled through call",
                "Scheduled through email, not Calendly",
                "Scheduled for an alternate time outside Calendly",
                "Not scheduled yet / Need to offer times",
            ],
        )

        manual_methods = [
            "Scheduled through call",
            "Scheduled through email, not Calendly",
            "Scheduled for an alternate time outside Calendly",
            "Not scheduled yet / Need to offer times",
        ]

        if scheduling_method == "Scheduled through Calendly":
            card(
                "Calendly Appointment",
                """
                Calendly automatically handles some steps, but RAs still need to update the database and calendar.
                """,
                "schedule",
            )

            card(
                "Emails",
                """
                <ul class="checklist">
                    <li>Calendly automatically sends a confirmation email immediately after sign-up.</li>
                    <li>Calendly automatically sends a reminder email 24 hours before the appointment.</li>
                    <li><b>RAs should not send confirmation or reminder emails manually.</b></li>
                </ul>
                """,
                "email",
            )

            card(
                "24-Hour Reminder Call",
                """
                <ul class="checklist">
                    <li>Call the family 24 hours before the appointment as an additional reminder, if a phone number is available.</li>
                </ul>
                """,
                "phone",
            )

            card(
                "Google Calendar",
                """
                A calendar event will automatically be created in the BCD Lab calendar.
                <br><br>
                RAs should edit the calendar event:
                <ul class="checklist">
                    <li>Replace the title with <b>[Study code] - [Child ID in database]</b>.</li>
                    <li>Example: <b>[EBOX] - L2000</b></li>
                    <li>Delete the parent name/email and child name from the beginning of the description.</li>
                    <li>Keep everything else in the description.</li>
                </ul>
                """,
                "schedule",
            )

            card(
                "Database",
                """
                <ul class="checklist">
                    <li>Manually enter the appointment into the database.</li>
                </ul>
                """,
                "neutral",
            )

            scheduling_tasks = [
                "Do not send a manual confirmation email",
                "Do not send a manual reminder email",
                "Call the family 24 hours before the appointment, if phone number is available",
                "Confirm the Google Calendar event was created automatically",
                "Rename calendar title to [Study code] - [Child ID in database]",
                "Delete parent name/email and child name from the beginning of the calendar description",
                "Keep the rest of the calendar description",
                "Manually enter the appointment into the database",
            ]
            scheduling_next = "Calendly handles emails automatically. RA responsibilities are the 24-hour call, calendar cleanup, and database entry."

        elif scheduling_method in manual_methods:
            if scheduling_method == "Not scheduled yet / Need to offer times":
                card(
                    "Before Offering Times",
                    """
                    Preview study-specific availability on Google Calendar before contacting the family.
                    <br><br>
                    Offer times in this order:
                    <ol>
                        <li>Offer fixed times first.</li>
                        <li>By default, initially offer <b>9:00 AM–3:00 PM</b> availability, even if later times are available in Calendar.</li>
                        <li>If 9:00 AM–3:00 PM does not work, offer later weekday times.</li>
                        <li>If all weekday times do not work, check with the lab team first, then offer weekend times if approved.</li>
                        <li>If no times work, ask whether the family would like to be contacted again in <b>2–3 months</b>, if the child will not age out.</li>
                    </ol>
                    """,
                    "warning",
                )

                scheduling_tasks = [
                    "Preview study-specific availability on Google Calendar",
                    "Offer fixed times first",
                    "Initially offer 9:00 AM–3:00 PM availability",
                    "If needed, offer later weekday times",
                    "If needed, check with lab team before offering weekend times",
                    "If no times work, ask about contacting again in 2–3 months if the child does not age out",
                ]
                scheduling_next = "After the family schedules, select the relevant manual scheduling option above."

            else:
                card(
                    "Manual Scheduling Appointment",
                    """
                    Use this workflow when the participant schedules through call, schedules through email outside Calendly, or schedules an alternate time after Calendly times do not work.
                    """,
                    "schedule",
                )

                card(
                    "Before Scheduling",
                    """
                    <ul class="checklist">
                        <li>Preview study-specific availability on Google Calendar before contacting.</li>
                        <li>Offer fixed times first.</li>
                        <li>By default, initially offer <b>9:00 AM–3:00 PM</b> availability, even if later times are available in Calendar.</li>
                        <li>If that availability does not work, offer later weekday times.</li>
                        <li>If all weekday times do not work, check with the lab team first before offering weekend times.</li>
                        <li>If no times work, ask whether the family would like to be contacted again in <b>2–3 months</b>, if the child does not age out.</li>
                    </ul>
                    """,
                    "warning",
                )

                card(
                    "Emails and Reminder Call",
                    """
                    RAs should manually:
                    <ul class="checklist">
                        <li>Send a confirmation email immediately after the parent schedules.</li>
                        <li>Send a reminder email at least 24 hours before the appointment time.</li>
                        <li>Call the parent 24 hours in advance as an additional reminder, if a phone number is available.</li>
                    </ul>
                    """,
                    "email",
                )

                card(
                    "FileMaker Pro and Spreadsheet",
                    """
                    Update the FileMaker Pro database in both places:
                    <ul class="checklist">
                        <li>Appointment log.</li>
                        <li>Appointment info section in the top left.</li>
                    </ul>
                    Also update the separate database spreadsheet, if applicable.
                    """,
                    "neutral",
                )

                card(
                    "Google Calendar",
                    """
                    Manually add the appointment to the Google Calendar.
                    <br><br>
                    Calendar title:
                    <ul class="checklist">
                        <li><b>[Study code] - [Child ID in database]</b></li>
                        <li>Example: <b>[EBOX] - L2000</b></li>
                    </ul>
                    Calendar description should include:
                    <ul class="checklist">
                        <li>Number of accompanying siblings.</li>
                        <li>Make and model of the vehicle they will be arriving in.</li>
                    </ul>
                    """,
                    "schedule",
                )

                scheduling_tasks = [
                    "Preview study-specific availability on Google Calendar",
                    "Offer fixed times first",
                    "Initially offer 9:00 AM–3:00 PM availability",
                    "Send confirmation email immediately after parent schedules",
                    "Send reminder email at least 24 hours before appointment",
                    "Call parent 24 hours before appointment, if phone number is available",
                    "Update FileMaker Pro appointment log",
                    "Update FileMaker Pro appointment info section in the top left",
                    "Update separate database spreadsheet, if applicable",
                    "Manually add appointment to Google Calendar",
                    "Title calendar event as [Study code] - [Child ID in database]",
                    "Add number of accompanying siblings to calendar description",
                    "Add vehicle make and model to calendar description",
                ]
                scheduling_next = "Manual scheduling requires manual confirmation email, reminder email, reminder call, FileMaker updates, spreadsheet updates if applicable, and Google Calendar entry."

    with task_col:
        card(
            "Scheduling Task List",
            "<p class='small'>Complete the relevant checklist for this scheduling situation.</p>",
            "neutral",
        )
        checklist(scheduling_tasks)
        st.info(scheduling_next)

# -----------------------------
# Quick Reference Tab
# -----------------------------
with quick_reference_tab:
    st.header("One-Screen Quick Reference")

    st.subheader("Contact Workflow")
    st.markdown(
        """
| Situation | What RA should do |
|---|---|
| Family prefers email | Email only. Do not call or text. |
| Phone path, first call, no answer | Leave voicemail + First Contact Email + First Contact Text |
| Phone path, follow-ups #2–#5 | Call, no voicemail + Follow-up Email + Follow-up Text |
| Email path, contact #1 | First Contact Email with Calendly link |
| Email path, follow-ups #2–#5 | Follow-up Email only |
| After 5th contact, phone path | Wait 3 days → Next-Month Email + Next-Month Text |
| After 5th contact, email path | Wait 3 days → Next-Month Email only |
        """
    )

    st.subheader("Scheduling & Reminders")
    st.markdown(
        """
| Situation | What RA should do |
|---|---|
| Calendly sign-up | Do not manually send confirmation/reminder emails. Calendly does this automatically. |
| Calendly sign-up | Call 24 hours before appointment, if phone number is available. |
| Calendly sign-up | Edit calendar title to `[Study code] - [Child ID in database]`. |
| Calendly sign-up | Remove parent/child names from beginning of calendar description; keep everything else. |
| Calendly sign-up | Manually enter appointment into database. |
| Manual scheduling | Preview Google Calendar before contacting. |
| Manual scheduling | Offer fixed 9 AM–3 PM times first. |
| Manual scheduling | If needed, offer later weekdays; if needed, ask lab before weekend times. |
| Manual scheduling | Send confirmation email immediately after scheduling. |
| Manual scheduling | Send reminder email at least 24 hours before appointment. |
| Manual scheduling | Call 24 hours before appointment, if phone number available. |
| Manual scheduling | Update FileMaker log and appointment info; update separate spreadsheet if applicable. |
| Manual scheduling | Manually add event to Google Calendar with title `[Study code] - [Child ID in database]`. |
| Manual scheduling | Add siblings and vehicle make/model to calendar description. |
        """
    )

st.caption("BCD Lab internal workflow draft. Confirm template names and timing with the finalized lab SOP.")