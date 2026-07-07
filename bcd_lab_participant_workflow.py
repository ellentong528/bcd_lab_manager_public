# bcd_lab_contacting_protocol_app.py
# Run with: streamlit run bcd_lab_contacting_protocol_app.py

import streamlit as st

st.set_page_config(
    page_title="BCD Lab Contacting Protocol",
    page_icon="🧠",
    layout="wide",
)

# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
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

.blue { border-left: 8px solid #2563eb; }
.purple { border-left: 8px solid #7c3aed; }
.green { border-left: 8px solid #16a34a; }
.orange { border-left: 8px solid #f59e0b; }
.red { border-left: 8px solid #dc2626; }
.gray { border-left: 8px solid #64748b; }

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

.timeline {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin: 1rem 0 1.2rem 0;
}

.timeline-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 10px 13px;
    font-weight: 700;
    font-size: 14px;
}

.arrow {
    color: #64748b;
    font-weight: 900;
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

.checklist li {
    margin-bottom: 8px;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------
def card(title: str, body: str, style: str = "gray") -> None:
    st.markdown(
        f"""
<div class="card {style}">
    <h3>{title}</h3>
    <div>{body}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def make_checklist(items, prefix):
    for i, item in enumerate(items):
        st.checkbox(item, key=f"{prefix}_{i}_{item}")


def reset_all():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


def timeline(labels):
    html = '<div class="timeline">'
    for i, label in enumerate(labels):
        html += f'<div class="timeline-box">{label}</div>'
        if i < len(labels) - 1:
            html += '<div class="arrow">→</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="app-title">BCD Lab Contacting Protocol</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Interactive SOP for recruitment contact, follow-up timing, scheduling, reminders, and documentation.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Core Rules")
    st.markdown(
        """
**Contact timing**  
Wait **3–5 days** between contact attempts.

**After Contact #5**  
Wait **3–5 days**, then send next-month outreach.

**Email preference**  
If family prefers email, use **email only**.

**Voicemail rule**  
Only leave voicemail during the **first phone outreach**.

**Calling rule**  
No calls before **9:00 AM**.  
Maximum **one call per day per subject**.

**Logging rule**  
Record every interaction in FileMaker.
        """
    )
    st.divider()
    if st.button("Reset all checkboxes"):
        reset_all()

tabs = st.tabs([
    "Start Here",
    "Contact Workflow",
    "Scheduling & Reminders",
    "Logging Guide",
    "Quick Reference",
])

# -----------------------------
# Start Here
# -----------------------------
with tabs[0]:
    st.header("Start Here: Before Contacting")

    left, right = st.columns([2, 1])

    with left:
        card(
            "Before you contact a family",
            """
            Complete these setup steps before beginning recruitment outreach.
            """,
            "gray",
        )

        setup_tasks = [
            "Open the BCD Lab Calendar.",
            "Open the study-specific availability calendar.",
            "Check whether the study has a separate database spreadsheet.",
            "If there is a separate spreadsheet, cross-check it with FileMaker.",
            "If there is no separate spreadsheet, search FileMaker using the study-specific age range.",
            "Start with the oldest eligible participant within the age range.",
            "Check the family's preferred contact method.",
        ]
        make_checklist(setup_tasks, "setup")

    with right:
        card(
            "Do not skip this",
            """
            <ul class="checklist">
                <li>No calling before <b>9:00 AM</b>.</li>
                <li>Maximum <b>one call per day</b> per subject.</li>
                <li>Every interaction must be logged in FileMaker.</li>
                <li>Double-check parent and child names before sending emails.</li>
            </ul>
            """,
            "orange",
        )

    st.divider()
    st.subheader("Overall Recruitment Timeline")
    timeline([
        "Contact #1",
        "Wait 3–5 days",
        "Contact #2",
        "Wait 3–5 days",
        "Contact #3",
        "Wait 3–5 days",
        "Contact #4",
        "Wait 3–5 days",
        "Contact #5",
        "Wait 3–5 days",
        "Next-Month Outreach",
        "Pause at least 30 days",
    ])

# -----------------------------
# Contact Workflow
# -----------------------------
with tabs[1]:
    st.header("Contact Workflow")
    st.write("Use this section to decide exactly what to do for each contact attempt.")

    col_main, col_tasks = st.columns([2, 1])

    with col_main:
        preference = st.radio(
            "What is the family's preferred contact method?",
            ["No preference / Prefers calls", "Prefers email"],
            horizontal=True,
        )

        st.divider()

        if preference == "No preference / Prefers calls":
            card(
                "Phone / No Preference Path",
                """
                Use this path if the family has no listed preference or prefers calls.
                <br><br>
                <span class="pill">Call</span>
                <span class="pill">Email</span>
                <span class="pill">Text</span>
                """,
                "blue",
            )

            stage = st.radio(
                "Which stage are you in?",
                [
                    "Contact Attempt #1",
                    "Contact Attempts #2–#5",
                    "After Contact Attempt #5",
                    "Family responded",
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
                        "Contact Attempt #1: Call first",
                        """
                        <ul class="checklist">
                            <li>Call using the study-specific calling script.</li>
                            <li>Have the correct project script ready.</li>
                        </ul>
                        """,
                        "blue",
                    )
                    tasks = ["Call using the study-specific calling script."]
                    next_step = "If answered, follow the study script. If no answer, leave voicemail, send first-contact email, and send first-contact text."

                elif answered == "Yes":
                    card(
                        "Family answered",
                        """
                        <ul class="checklist">
                            <li>Follow the study-specific script.</li>
                            <li>If they schedule, go to Scheduling & Reminders.</li>
                        </ul>
                        """,
                        "green",
                    )
                    tasks = ["Follow the study-specific script.", "If scheduled, complete Scheduling & Reminders."]
                    next_step = "Move to Scheduling & Reminders if they schedule."

                else:
                    card(
                        "No answer during Contact Attempt #1",
                        """
                        Complete all three:
                        <ul class="checklist">
                            <li>Leave voicemail.</li>
                            <li>Send First Contact Email with experiment-specific Calendly link.</li>
                            <li>Send First Contact Text.</li>
                        </ul>
                        <p><b>Then:</b> wait <b>3–5 days</b> before Contact Attempt #2.</p>
                        """,
                        "orange",
                    )
                    tasks = [
                        "Leave voicemail.",
                        "Send First Contact Email with Calendly link.",
                        "Send First Contact Text.",
                    ]
                    next_step = "Wait 3–5 days before Contact Attempt #2."

            elif stage == "Contact Attempts #2–#5":
                attempt = st.selectbox(
                    "Which contact attempt are you making today?",
                    ["#2", "#3", "#4", "#5"],
                )

                card(
                    f"Contact Attempt {attempt}",
                    """
                    Only do this if <b>3–5 days</b> have passed since the previous contact attempt.
                    <br><br>
                    Complete all three:
                    <ul class="checklist">
                        <li>Call the family.</li>
                        <li><b>Do not leave voicemail.</b></li>
                        <li>Send Follow-up Email with experiment-specific Calendly link.</li>
                        <li>Send Follow-up Text immediately after the call.</li>
                    </ul>
                    """,
                    "blue",
                )

                tasks = [
                    "Confirm 3–5 days have passed since the previous contact.",
                    "Call the family.",
                    "Do not leave voicemail.",
                    "Send Follow-up Email with Calendly link.",
                    "Send Follow-up Text immediately after the call.",
                ]

                if attempt == "#5":
                    card(
                        "If there is still no response after Contact Attempt #5",
                        """
                        Wait <b>3–5 days</b>, then:
                        <ul class="checklist">
                            <li>Send Next-Month Text.</li>
                            <li>Send Next-Month Email.</li>
                            <li>Pause contact for at least 30 days unless instructed otherwise.</li>
                        </ul>
                        """,
                        "orange",
                    )
                    next_step = "If no response after Contact #5, wait 3–5 days, then send next-month text and email."
                else:
                    next_num = int(attempt.replace("#", "")) + 1
                    next_step = f"If no response, wait 3–5 days before Contact Attempt #{next_num}."

            elif stage == "After Contact Attempt #5":
                card(
                    "After Contact Attempt #5",
                    """
                    Use this only if the family still has not responded after Contact Attempt #5.
                    <br><br>
                    <span class="step-label">Wait 3–5 days after Contact #5</span>
                    <ul class="checklist">
                        <li>Send Next-Month Text.</li>
                        <li>Send Next-Month Email.</li>
                        <li>Pause contact for at least 30 days unless instructed otherwise.</li>
                    </ul>
                    """,
                    "red",
                )
                tasks = [
                    "Confirm 3–5 days have passed since Contact #5.",
                    "Send Next-Month Text.",
                    "Send Next-Month Email.",
                    "Pause contact for at least 30 days unless instructed otherwise.",
                ]
                next_step = "Pause contact for at least 30 days unless instructed otherwise."

            else:
                card(
                    "Family responded",
                    """
                    <ul class="checklist">
                        <li>Follow the study-specific script.</li>
                        <li>If they schedule, move to Scheduling & Reminders.</li>
                    </ul>
                    """,
                    "green",
                )
                tasks = ["Follow the study-specific script.", "If scheduled, complete Scheduling & Reminders."]
                next_step = "Move to Scheduling & Reminders if they schedule."

        else:
            card(
                "Email-Only Path",
                """
                Use this path if the family prefers email.
                <br><br>
                <b>Do not call or text unless the family later requests another contact method.</b>
                <br><br>
                <span class="pill">Email only</span>
                """,
                "purple",
            )

            stage = st.radio(
                "Which stage are you in?",
                [
                    "Contact Attempt #1",
                    "Contact Attempts #2–#5",
                    "After Contact Attempt #5",
                    "Family responded",
                ],
            )

            if stage == "Contact Attempt #1":
                card(
                    "Contact Attempt #1: Email only",
                    """
                    <ul class="checklist">
                        <li>Send First Contact Email.</li>
                        <li>Include the experiment-specific Calendly link.</li>
                    </ul>
                    <p><b>Then:</b> wait <b>3–5 days</b> before Contact Attempt #2.</p>
                    """,
                    "purple",
                )
                tasks = [
                    "Send First Contact Email.",
                    "Include experiment-specific Calendly link.",
                ]
                next_step = "Wait 3–5 days before Contact Attempt #2."

            elif stage == "Contact Attempts #2–#5":
                attempt = st.selectbox(
                    "Which email attempt are you sending today?",
                    ["#2", "#3", "#4", "#5"],
                )

                card(
                    f"Email Contact Attempt {attempt}",
                    """
                    Only do this if <b>3–5 days</b> have passed since the previous email.
                    <br><br>
                    <ul class="checklist">
                        <li>Send Follow-up Email.</li>
                        <li>Include the experiment-specific Calendly link.</li>
                        <li>Do not call.</li>
                        <li>Do not text.</li>
                    </ul>
                    """,
                    "purple",
                )

                tasks = [
                    "Confirm 3–5 days have passed since the previous email.",
                    "Send Follow-up Email.",
                    "Include experiment-specific Calendly link.",
                    "Do not call.",
                    "Do not text.",
                ]

                if attempt == "#5":
                    card(
                        "If there is still no response after Contact Attempt #5",
                        """
                        Wait <b>3–5 days</b>, then:
                        <ul class="checklist">
                            <li>Send Next-Month Email.</li>
                            <li>Do not call.</li>
                            <li>Do not text.</li>
                            <li>Pause contact for at least 30 days unless instructed otherwise.</li>
                        </ul>
                        """,
                        "orange",
                    )
                    next_step = "If no response after Contact #5, wait 3–5 days, then send next-month email."
                else:
                    next_num = int(attempt.replace("#", "")) + 1
                    next_step = f"If no response, wait 3–5 days before Contact Attempt #{next_num}."

            elif stage == "After Contact Attempt #5":
                card(
                    "After Contact Attempt #5",
                    """
                    Use this only if the family still has not responded after Contact Attempt #5.
                    <br><br>
                    <span class="step-label">Wait 3–5 days after Contact #5</span>
                    <ul class="checklist">
                        <li>Send Next-Month Email.</li>
                        <li>Do not call.</li>
                        <li>Do not text.</li>
                        <li>Pause contact for at least 30 days unless instructed otherwise.</li>
                    </ul>
                    """,
                    "red",
                )
                tasks = [
                    "Confirm 3–5 days have passed since Contact #5.",
                    "Send Next-Month Email.",
                    "Do not call.",
                    "Do not text.",
                    "Pause contact for at least 30 days unless instructed otherwise.",
                ]
                next_step = "Pause contact for at least 30 days unless instructed otherwise."

            else:
                card(
                    "Family responded",
                    """
                    <ul class="checklist">
                        <li>Reply by email unless the family requests another contact method.</li>
                        <li>Follow the study-specific script.</li>
                        <li>If they schedule, move to Scheduling & Reminders.</li>
                    </ul>
                    """,
                    "green",
                )
                tasks = [
                    "Reply by email unless they request another contact method.",
                    "Follow the study-specific script.",
                    "If scheduled, complete Scheduling & Reminders.",
                ]
                next_step = "Move to Scheduling & Reminders if they schedule."

    with col_tasks:
        card(
            "Today’s Checklist",
            "<p class='small'>Complete these tasks based on your selections.</p>",
            "gray",
        )
        make_checklist(tasks, "contact_tasks")
        st.info(next_step)

# -----------------------------
# Scheduling & Reminders
# -----------------------------
with tabs[2]:
    st.header("Scheduling & Reminders")
    st.write("Use this section once a family has scheduled or is actively scheduling.")

    sched_col, task_col = st.columns([2, 1])

    with sched_col:
        method = st.radio(
            "How was the appointment scheduled?",
            [
                "Scheduled through Calendly",
                "Scheduled through call",
                "Scheduled through email, not Calendly",
                "Scheduled for alternate time outside Calendly",
                "Not scheduled yet / Need to offer times",
            ],
        )

        if method == "Scheduled through Calendly":
            card(
                "Calendly Appointment",
                """
                Calendly handles confirmation and reminder emails automatically.
                """,
                "green",
            )

            card(
                "Emails",
                """
                <ul class="checklist">
                    <li>Calendly automatically sends the confirmation email immediately after sign-up.</li>
                    <li>Calendly automatically sends the reminder email 24 hours before the appointment.</li>
                    <li><b>RAs should not send confirmation or reminder emails manually.</b></li>
                </ul>
                """,
                "purple",
            )

            card(
                "Reminder Call",
                """
                <ul class="checklist">
                    <li>Call the family 24 hours before the appointment as an additional reminder, if a phone number is available.</li>
                </ul>
                """,
                "blue",
            )

            card(
                "Calendar",
                """
                A Google Calendar event is created automatically.
                <br><br>
                Edit the event:
                <ul class="checklist">
                    <li>Rename title to <b>[Study code] - [Child ID in database] – [Timepoint + Visit]</b>.</li>
                    <li>Example: <b>[LUNCH] L2000 (Time 2 Visit 1)</b></li>
                    <li>Delete parent name/email and child name from the beginning of the description.</li>
                    <li>Keep everything else in the description.</li>
                </ul>
                """,
                "green",
            )

            card(
                "Database",
                """
                <ul class="checklist">
                    <li>Manually enter the appointment into FileMaker.</li>
                </ul>
                """,
                "gray",
            )

            sched_tasks = [
                "Do not send manual confirmation email.",
                "Do not send manual reminder email.",
                "Call family 24 hours before appointment, if phone number is available.",
                "Confirm calendar event was created automatically.",
                "Rename calendar title to [Study code] - [Child ID] – [Timepoint + Visit].",
                "Delete parent name/email and child name from beginning of description.",
                "Keep the rest of the calendar description.",
                "Manually enter appointment into FileMaker.",
            ]
            sched_next = "Calendly handles emails. RA handles reminder call, calendar cleanup, and FileMaker entry."

        elif method == "Not scheduled yet / Need to offer times":
            card(
                "Before Offering Appointment Times",
                """
                Preview study-specific availability on Google Calendar before contacting the family.
                <br><br>
                Offer times in this order:
                <ol>
                    <li>Offer fixed times first.</li>
                    <li>Initially offer <b>9:00 AM–3:00 PM</b> availability.</li>
                    <li>If that does not work, offer later weekday times.</li>
                    <li>If weekday times do not work, check with the lab team before offering weekend times.</li>
                    <li>If no times work, ask whether the family would like to be contacted again in <b>2–3 months</b>, if the child will not age out.</li>
                </ol>
                """,
                "orange",
            )

            sched_tasks = [
                "Preview study-specific Google Calendar availability.",
                "Offer fixed times first.",
                "Initially offer 9:00 AM–3:00 PM availability.",
                "If needed, offer later weekday times.",
                "If needed, check with lab team before offering weekend times.",
                "If no times work, ask about recontacting in 2–3 months if child does not age out.",
            ]
            sched_next = "After the family schedules, select the appropriate scheduling method above."

        else:
            card(
                "Manual Scheduling",
                """
                Use this path when the appointment was scheduled by call, email outside Calendly, or alternate time outside Calendly.
                """,
                "green",
            )

            card(
                "Before Scheduling",
                """
                <ul class="checklist">
                    <li>Preview study-specific availability on Google Calendar before contacting.</li>
                    <li>Offer fixed times first.</li>
                    <li>Initially offer <b>9:00 AM–3:00 PM</b> availability, even if later times are available.</li>
                    <li>If that does not work, offer later weekday times.</li>
                    <li>If weekday times do not work, check with the lab team before offering weekend times.</li>
                    <li>If no times work, ask whether the family would like to be contacted again in <b>2–3 months</b>, if the child will not age out.</li>
                </ul>
                """,
                "orange",
            )

            card(
                "Emails and Reminder Call",
                """
                RAs manually complete:
                <ul class="checklist">
                    <li>Send confirmation email immediately after parent schedules.</li>
                    <li>Send reminder email at least 24 hours before appointment time.</li>
                    <li>Call parent 24 hours in advance as an additional reminder, if phone number is available.</li>
                </ul>
                """,
                "purple",
            )

            card(
                "FileMaker and Spreadsheet",
                """
                Update:
                <ul class="checklist">
                    <li>FileMaker appointment log.</li>
                    <li>FileMaker appointment info section in the top left.</li>
                    <li>Separate database spreadsheet, if applicable.</li>
                </ul>
                """,
                "gray",
            )

            card(
                "Google Calendar",
                """
                Manually add the appointment to Google Calendar.
                <br><br>
                Event title:
                <ul class="checklist">
                    <li><b>[Study code] - [Child ID in database]</b></li>
                </ul>
                Event description:
                <ul class="checklist">
                    <li>Number of accompanying siblings.</li>
                    <li>Make and model of vehicle they will be arriving in.</li>
                </ul>
                """,
                "green",
            )

            sched_tasks = [
                "Preview study-specific Google Calendar availability.",
                "Offer fixed times first.",
                "Initially offer 9:00 AM–3:00 PM availability.",
                "Send confirmation email immediately after scheduling.",
                "Send reminder email at least 24 hours before appointment.",
                "Call parent 24 hours before appointment, if phone number is available.",
                "Update FileMaker appointment log.",
                "Update FileMaker appointment info section.",
                "Update separate database spreadsheet, if applicable.",
                "Manually add appointment to Google Calendar.",
                "Title event as [Study code] - [Child ID in database].",
                "Add number of accompanying siblings to event description.",
                "Add vehicle make/model to event description.",
            ]
            sched_next = "Manual scheduling requires manual emails, call reminder, FileMaker update, spreadsheet update if applicable, and calendar entry."

    with task_col:
        card(
            "Scheduling Checklist",
            "<p class='small'>Complete the relevant tasks for this scheduling situation.</p>",
            "gray",
        )
        make_checklist(sched_tasks, "sched_tasks")
        st.info(sched_next)

# -----------------------------
# Logging Guide
# -----------------------------
with tabs[3]:
    st.header("FileMaker Logging Guide")

    card(
        "Every interaction must be logged",
        """
        Every log should include:
        <ul class="checklist">
            <li><b>Study code</b></li>
            <li><b>Interaction recorded</b></li>
            <li><b>RA initials</b></li>
            <li><b>Date/time of interaction</b></li>
        </ul>
        """,
        "gray",
    )

    st.subheader("Example log format")
    st.code("[3MUG] participant scheduled for 08/17/2024 at 10:00am…FSH, 08/15/2024 11:33am.")

    st.subheader("Common log categories")
    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "Phone",
            """
            <ul class="checklist">
                <li>Answered call</li>
                <li>Unanswered call</li>
                <li>Left voicemail</li>
                <li>No answer/no voicemail</li>
                <li>Phone disconnected</li>
                <li>Participant hung up</li>
            </ul>
            """,
            "blue",
        )

    with col2:
        card(
            "Text / Email",
            """
            <ul class="checklist">
                <li>Text</li>
                <li>Left text message</li>
                <li>First contact email</li>
                <li>Follow-up email</li>
                <li>Participant replied</li>
                <li>Reminder email sent</li>
            </ul>
            """,
            "purple",
        )

    with col3:
        card(
            "Scheduling / Status",
            """
            <ul class="checklist">
                <li>Scheduled</li>
                <li>Parent scheduled through Calendly</li>
                <li>No longer interested</li>
                <li>Asked to be removed</li>
                <li>Moved out of area</li>
                <li>Other relevant details</li>
            </ul>
            """,
            "green",
        )

# -----------------------------
# Quick Reference
# -----------------------------
with tabs[4]:
    st.header("Quick Reference")

    st.subheader("Contact Workflow")
    st.markdown(
        """
| Situation | What to do |
|---|---|
| Family prefers email | Email only. Do not call or text. |
| First phone call, no answer | Leave voicemail + First Contact Email + First Contact Text |
| Phone follow-ups #2–#5 | Call, no voicemail + Follow-up Email + Follow-up Text |
| Email contact #1 | First Contact Email with Calendly link |
| Email follow-ups #2–#5 | Follow-up Email only |
| After Contact #5, phone path | Wait 3–5 days → Next-Month Text + Next-Month Email |
| After Contact #5, email path | Wait 3–5 days → Next-Month Email only |
| After next-month outreach | Pause at least 30 days unless instructed otherwise |
        """
    )

    st.subheader("Scheduling")
    st.markdown(
        """
| Situation | What to do |
|---|---|
| Calendly sign-up | Do not send confirmation/reminder emails manually |
| Calendly sign-up | Call 24 hours before appointment, if phone number available |
| Calendly sign-up | Edit calendar title and clean beginning of description |
| Calendly sign-up | Manually enter appointment into FileMaker |
| Manual scheduling | Preview Google Calendar first |
| Manual scheduling | Offer fixed 9 AM–3 PM times first |
| Manual scheduling | Send confirmation email immediately |
| Manual scheduling | Send reminder email at least 24 hours before |
| Manual scheduling | Call 24 hours before, if phone number available |
| Manual scheduling | Update FileMaker, spreadsheet if applicable, and Google Calendar |
        """
    )

    st.subheader("Email format reminders")
    st.markdown(
        """
- First contact email subject: **New Study for [CHILD’S NAME] at the BCD Lab**
- Appointment confirmation email subject: **Confirmation for [CHILD’S NAME]'s BCD Lab Appointment**
- Reminder email should reply to the confirmation email.
- Always double-check parent names, child names, dates, and times before sending.
        """
    )

st.caption("BCD Lab internal workflow tool. Timing updated to 3–5 days between contact attempts, including after Contact #5.")
