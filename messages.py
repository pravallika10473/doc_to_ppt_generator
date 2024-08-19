prompt1 ="""
Analyze the given document and extract key topics, following these guidelines:

1. Key Topic Identification:
   - Topics should represent major sections or themes in the document.
   - Each key topic should be substantial enough for at least one slide with 3-5 bullet points, potentially spanning multiple slides.
   - Topics should be broad enough to encompass multiple related points but specific enough to avoid overlap.
   - Identify topics in the order they appear in the document.
   - Consider a new topic when there's a clear shift in the main subject, signaled by transitional phrases, new headings, or a distinct change in content focus.
   - If a topic recurs, don't create a new entry unless it's substantially expanded upon.

2. Key Topic Documentation:
   - For each key topic, create a detailed name that sums up the idea of the section it represents. Then provide the two consecutive sentences from the start of the section or theme it represents.
   - These sentences should signal a shift to a new major theme or section, helping define where the new key topic begins.

3. Provide the output in the following format:
**<key topic 1>**
<two sentences where key topic 1 starts>
**<key topic 2>**
<two sentences where key topic 2 starts>

Document to analyze:

**<paste document content here>**

"""

prompt2= """
You will be given a key topic, its starting lines, the starting lines of the next topic (or "" if it's the last topic), and a complete document. Your task is to create slides based on the portion of the document between these starting lines. Follow these steps:

1. Identify the relevant section of the document between the given starting lines.
2. Analyze this section and create slides with titles and bullet points.

Guidelines:
- The number of slides can be as few as one and as many as 10, depending on the amount of non-repetitive information in the relevant section of the key topic.
- Present slides in the order that the information appears in the document.
- Each slide should have 4-6 concise bullet points, each containing a single key idea or fact.
- Use concise phrases or short sentences for bullet points, focusing on conveying key information clearly and succinctly.
- If information seems relevant to multiple topics, include it in the current topic's slides, as it appears first in the document.
- Avoid redundancy across slides within the same key topic.

Output Format:
**<slide 1 title>**
<point 1 of slide 1>
<point 2 of slide 1>
<point 3 of slide 1>
**<slide 2 title>**
<point 1 of slide 2>
<point 2 of slide 2>
<point 3 of slide 2>
<point 4 of slide 2>


Inputs:
Key Topic: '''{{keytopic}}'''
Starting Lines for This Topic: '''{{startingLines}}'''
Starting Lines for Next Topic : '''{{nextTopicStartingLines}}'''

Document:

{{pasteFullDoc}}


Please create slides based on the section of the document between the given starting lines, following the guidelines provided. Ensure that the slides comprehensively cover the key topic without unnecessary repetition.
"""