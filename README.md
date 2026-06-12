# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
      I chose a Medical Assistant Study Guide Chatbot. As a Medical Assistant, there is a lot of information that you're supposed to be aware of in order to gain your license. This information can stretch from medical terminology to how to interpret an EKG. Oftentimes I was surrounded by 5 different books and wanted to streamline the process by creating a chatbot that has all the information one needs to study. Instead of having a billion tabs or textbooks open, you can ahve one tab open with all the information you need.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description                                  | URL or location |
|---|--------|----------------------------------------------|-----------------|
| 1 | | | |    Vital Signs: blood pressure, purlse rate, etc  https://www.hopkinsmedicine.org/health/conditions-and-diseases/vital-signs-body-temperature-pulse-rate-respiration-rate-blood-pressure 

| 2 | | | |   Common Medical Terms                          https://www.rcog.org.uk/for-the-public/a-z-of-medical-terms/ 

| 3 | | | |   Anatomy and Physiology                        https://www.cliffsnotes.com/study-guides/anatomy-and-physiology 

| 4 | | | |   Common Medical Abbreviations                  https://www.asha.org/practice-portal/professional-issues/documentation-in-health-care/common-medical-abbreviations/?srsltid=AfmBOor_F8eVZTVh6MNF_-8R9-aPP78Ms8feFN0Zy96HDKYZEZDVmXIa 

| 5 | | | |  OSHA Healthcare Standards                      https://www.cdc.gov/niosh/learning/safetyculturehc/module-5/5.html 

| 6 | | | |  HIPPA Training Requirements                    https://www.hipaajournal.com/hipaa-training-requirements/ 

| 7 | | | |  Phlebotomy Guide                               https://phlebotomyusa.com/blog/phlebotomy/a-step-by-step-guide-to-phlebotomy-procedure/ 

| 8 | | | |  EKG Basics                                     https://www.aclsmedicaltraining.com/basics-of-ecg 

| 9 | | | |  Common Lab Procedure & Their Meaning           https://www.parentprojectmd.org/wp-content/uploads/2021/02/Common_Labs.pdf 

| 10 | | | | Beside Manner & Patient Interaction            https://med.stanford.edu/stanfordmedicine25/blog/archive/20240/bedside-communication-tips.html 

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
     500 characters
**Overlap:**
     50 characters
**Why these choices fit your documents:**
     I chose 500 character chunks with 50 overlap because my documents vary from just including short definitions to long precedural paragraphs. I initally had the overlap at 100 but a lot of the information was being cutoff so i reduced it to 50 which gave better chunk outputs
**Final chunk count:**
     517 chunks

**Sample Chunks:**

====================================================================================================
QUERY: What does HIPAA stand for?
====================================================================================================

--- Retrieved Chunk ---
Source: HIPAA Training Requirements - Updated for 2026.pdf
Chunk Index: 347
Distance: 0.7110099196434021
thcare and understand the compliance
oﬃcer’s role.
Deﬁnitions and Lexicons
This module should provide deﬁnitions of frequently used “HIPAA terms” such as PHI, ePHI, Minimum Necessary, Covered Entity, Business
Associate, and Healthcare Operations. The module should be available for all staﬀ but can be optional for staﬀ who have already worked in
healthcare and understand HIPAA terminology.

--- Retrieved Chunk ---
Source: HIPAA Training Requirements - Updated for 2026.pdf
Chunk Index: 458
Distance: 0.7201915383338928
from over
ten years of our HIPAA breach reporting.
View The HIPAA Journal Training
The Gold Standard in HIPAA Training
by The HIPAA Journal Team
CEUs & Certiﬁcates | Completion Tracking
View HIPAA Training for Individuals
   
 
About The HIPAA Journal
The HIPAA Journal is the leading source of information on the Health Insurance Portability and Accountability Act (HIPAA), providing the best-available HIPAA
Training and news coverage of regulatory developments, enforcement actions, data

--- Retrieved Chunk ---
Source: HIPAA Training Requirements - Updated for 2026.pdf
Chunk Index: 448
Distance: 0.7395718097686768
d to individuals who pass a HIPAA training course. Often the courses are
designed to provide individuals with a basic knowledge of HIPAA so that subsequent training on (for example) policies and procedures or
security and awareness is more understandable. HIPAA training certiﬁcates can also demonstrate to potential employers that a job
candidate has an understanding of the HIPAA rules and regulations.
Who is responsible for training students about HIPAA?

--- Retrieved Chunk ---
Source: HIPAA Training Requirements - Updated for 2026.pdf
Chunk Index: 398
Distance: 0.7607261538505554
Training Requirements FAQ
What is HIPAA training?
HIPAA training is part of the training new members of a covered entity’s workforce receive when they start working for a covered health
plan, healthcare clearinghouse, healthcare provider, or pharmacy. The training should include an explanation of terms such as Protected
Health Information and why it is necessary to protect the privacy of individually identiﬁable health information.

--- Retrieved Chunk ---
Source: HIPAA Training Requirements - Updated for 2026.pdf
Chunk Index: 388
Distance: 0.7607975006103516
ﬁers that make the health information “protected”.
Being a HIPAA Compliant Student
Students are responsible for understanding the covered entity’s HIPAA policies and procedures and following them just as a healthcare
professional would. They also need to know how to recognize a HIPAA violation and who to report it to.

====================================================================================================
QUERY: What is a normal adult heart rate?
====================================================================================================

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 490
Distance: 0.56020188331604
or the number of times the heart beats per minute. As the heart
pushes blood through the arteries, the arteries expand and contract with the �ow of the blood. Taking a pulse not only
measures the heart rate, but also can indicate the following:
The normal pulse for healthy adults ranges from 60 to 100 beats per minute. The pulse rate may �uctuate and increase
with exercise, illness, injury, and emotions. Females ages 12 and older , in general, tend to have faster heart rates than
do males.

--- Retrieved Chunk ---
Source: The Basics of ECG _ ACLS Medical Training.pdf
Chunk Index: 481
Distance: 0.8928333520889282
t corresponds to
heart rate of 300 beats a minute. The dark vertical lines
correspond to 300, 150, 100, 75, 60, and 50 bpm. For example, if
there are three large boxes between R waves, the patient’s heart
rate is 100 bpm. There are more accurate ways to determine
heart rate from ECG, but in life-saving scenarios, this method
provides a quick estimate.
Mastering EKG interpretation is the foundation of accurate
cardiac care.

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 496
Distance: 0.9336477518081665
note whether a person has any di�culty breathing.
Normal respiration rates for an adult person at rest range from 12 to 16 breaths per minute.
What is blood pressure?
Blood pressure is the force of the blood pushing against the artery walls during contraction and relaxation of the heart.

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 491
Distance: 1.0236773490905762
al, tend to have faster heart rates than
do males. Athletes, such as runners, who do a lot of cardiovascular conditioning, may have heart rates near 40 beats
per minute and experience no problems.
Temperatures taken rectally (using a glass or digital thermometer) tend to be 0.5 to 0.7 degrees F higher than
when taken by mouth.
Temperatures can be taken under the arm using a glass or digital thermometer . Temperatures taken by this
route tend to be 0.3 to 0.

--- Retrieved Chunk ---
Source: The Basics of ECG _ ACLS Medical Training.pdf
Chunk Index: 480
Distance: 1.070529580116272
n the T wave and the P wave, it
could be a U wave. The biological basis for a U wave is unknown.
There are many ways to determine a patient’s heart rate using
ECG. One of the quickest ways is called the sequence method.
To use the sequence method, �nd an R wave that lines up with
one of the dark vertical lines on the ECG paper. If the next R
wave appears on the next dark vertical line, it corresponds to
heart rate of 300 beats a minute.

====================================================================================================
QUERY: What are the steps for taking blood pressure?
====================================================================================================

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 509
Distance: 0.8861992955207825
tion, they are more expensive than other monitors.
Before you measure your blood pressure:
The American Heart Association recommends the following guidelines for home blood pressure monitoring:
Don't smoke or drink co�ee for 30 minutes before taking your blood pressure.
Go to the bathroom before the test.
Relax for 5 minutes before taking the measurement.
Sit with your back supported (don't sit on a couch or soft chair). Keep your feet on the �oor uncrossed.

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 510
Distance: 0.9337173700332642
soft chair). Keep your feet on the �oor uncrossed. Place your arm
on a solid �at surface (like a table) with the upper part of the arm at heart level. Place the middle of the cu� directly
above the bend of the elbow. Check the monitor's instruction manual for an illustration.
Take multiple readings. When you measure, take 2 to 3 readings one minute apart and record all the results.
Take your blood pressure at the same time every day, or as your healthcare provider recommends.

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 502
Distance: 1.1087714433670044
mal is not
necessarily an indication of a problem. Your doctor will want to see multiple blood pressure measurements over several
days or weeks before making a diagnosis of high blood pressure and starting treatment. Ask your provider when to
contact him or her if your blood pressure readings are not within the normal range.
Why should I monitor my blood pressure at home?

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 497
Distance: 1.1261069774627686
ls during contraction and relaxation of the heart.
Each time the heart beats, it pumps blood into the arteries, resulting in the highest blood pressure as the heart
Using the �rst and second �ngertips, press �rmly but gently on the arteries until you feel a pulse.
Begin counting the pulse when the clock's second hand is on the 12.
Count your pulse for 60 seconds (or for 15 seconds and then multiply by four to calculate beats per minute).

--- Retrieved Chunk ---
Source: Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pressure) _ Johns Hopkins Medicine.pdf
Chunk Index: 498
Distance: 1.1433310508728027
n multiply by four to calculate beats per minute).
When counting, do not watch the clock continuously, but concentrate on the beats of the pulse.
If unsure about your results, ask another person to count for you.
Vital Signs (Body Temperature, Pulse Rate, Respiration Rate, Blood Pre...  
 
contracts. When the heart relaxes, the blood pressure falls.
Two numbers are recorded when measuring blood pressure.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
     all-MiniLM-L6-v2 via sentence-transformers. this was the reccomended stack provided to me
**Production tradeoff reflection:**
     I would prefer a model trained on medical text since im making a medical assistant chatbox. It would also be cool to have multilingual support for students around the world
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
     The system prompt instructs the model to answer using only the retrieved document context."Answer the user's question using ONLY the information in the provided context. Do not use outside knowledge. Do not guess. If the context does not contain enough information, say: 'I don't have enough information on that.'" The retrieved chunks are inserted directly into the prompt before the user question, ensuring that the model receives only the relevant document content when generating a response.

**How source attribution is surfaced in the response:**
     Rather than relying on the LLM to cite sources, the chatbot automatically attaches the names of the retrieved documents and chunk information to each response. This guarantees that users can see which documents were used to answer their question and improves transparency in the system's responses.
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->
| # | Question                     | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|------------------------------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What does HIPAA stand for?    
          - Expected: Health Insurance Portability and Accountability Act 
          - System Response: Retrieved HIPAA-related training information and identified HIPAA as the Health Insurance Portability and Accountability Act. - Retrieval Quality: Relevant 
          - Response Accuracy: Semi-Accurate 

| 2 | What are the steps for taking blood pressure? 
          - Expected: Multi-step blood pressure procedure
          - System Response: Retrieved preparation and measurement instructions including sitting correctly, positioning the arm, placing the cuff, etc 
          - Retrieval Quality: Relevant
          - Accuracy: Accurate

| 3 | What is a normal adult heart rate? 
          - Expected: 60–100 beats per minute 
          - System Response: stated that a normal adult pulse ranges from 60–100 bpm. 
          - Retrieval Quality: Relevant\
          - Accuracy: Accurate

| 4 | What is hypertension? 
          - Expected: Consistently elevated blood pressure
          - System Response: Retrieved blood pressure and hypertension-related information explaining elevated blood pressure levels. 
          - Retrieval Quality: Partially Relevant
          - Accuracy: Partially Accurate

| 5 | What is the purpose of HIPAA? 
          - Expected: Protect patient privacy and health information 
          - System response: Retrieved HIPAA training and Protected Health Information (PHI) content explaining the protection of patient information
          - Retrieval Quality: Relevant 
          - Accuracy: Accurate 

**Retrieval quality:** Relevant  
**Response accuracy:** Accurate 

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed and what the system returned**
     This question didnt particullarly fail but when asked "What does HIPPA stand for?" The system returned: "The context does not explicitly state what HIPAA stands for, but Source 2 mentions "the Health Insurance Portability and Accountability Act (HIPAA)". Therefore, based on this information: HIPAA stands for the Health Insurance Portability and Accountability Act." While the information was not incorrect, the system did make an educated guess

**Root cause (tied to a specific pipeline stage):**
     This is tied to the documents pipeline. I didnt include a document that very clearly stated what HIPPA stood for. So that forced the system to make an educated guess based on the chunks it recieved. 
**What you would change to fix it:**
     This would entail include more documentation, specifically one that includes more abbreviations
---

## Spec Reflection

**One way the spec helped you during implementation:**

The planning document helped me break the project into manageable stages before writing any code. Having the chunking strategy, retrieval approach, and architecture diagram already defined made it easier to prompt AI tools for specific parts of the pipeline and verify that the generated code matched my intended design.

**One way your implementation diverged from the spec, and why:**

Initially, I planned to use websites directly as my document sources. During implementation, I downloaded the website content as PDF files and loaded them locally instead. This made document ingestion more reliable and simplified the cleaning process because the chatbot no longer depended on external websites being available.

---

## AI Usage

**Instance 1**

- *What I gave the AI:*  
  I provided my Documents section, Chunking Strategy, and pipeline architecture from planning.md and asked it to generate an ingestion and chunking script.

- *What it produced:*  
  It generated a script that loaded PDF documents, cleaned the extracted text, and split documents into chunks using my specified chunk size and overlap.

- *What I changed or overrode:*  
  After testing the output, I modified the cleaning function to remove additional PDF footer text, URLs, and formatting artifacts that were still appearing in retrieved chunks. I also changed the size of my overlap once I saw the chunk outputs

**Instance 2**

- *What I gave the AI:*  
  I provided my retrieval approach section and architecture diagram and asked it to generate embedding and retrieval code using all-MiniLM-L6-v2 and ChromaDB.

- *What it produced:*  
  It generated code that embedded document chunks, stored them in ChromaDB with metadata, and implemented a retrieval function that returned the top-k most relevant chunks and distance scores.

- *What I changed or overrode:*  
  I evaluated the retrieval results using my test questions and adjusted the document cleaning process to improve retrieval quality. I also inspected the retrieved chunks and verified that source metadata was preserved for attribution in the final chatbot responses.
