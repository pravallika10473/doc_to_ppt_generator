
prompt_prefix0="""
Please analyze the document provided and extract key topics suitable for presentation slides, following these steps:

 **Identify Key Topics**:
   - Focus on identifying the major themes or sections of the document.
   - Each key topic should be comprehensive enough to cover 2-3 bullet points on a slide, with the potential to extend across multiple slides.
   - Ensure topics are broad but distinct, avoiding any overlap.
   - Extract topics in the order they appear, marking any significant content shifts, such as new headings, transitions, or changes in focus.
   - Avoid duplicating topics unless they are revisited with substantial new information.
 
- Give only topic names as follows  
**Output Structure**: 
   - Format the output as follows :
     **<Topic 1 Name>**
     **<Topic 2 Name>**

"""
prompt_prefix1 = """
Please analyze the document provided and extract key topics suitable for presentation slides, following these steps:

1. **Identify Key Topics**:
   - Focus on identifying the major themes or sections of the document.
   - Each key topic should be comprehensive enough to cover 2-3 bullet points on a slide, with the potential to extend across multiple slides.
   - Ensure topics are broad but distinct, avoiding any overlap.
   - Extract topics in the order they appear, marking any significant content shifts, such as new headings, transitions, or changes in focus.
   - Avoid duplicating topics unless they are revisited with substantial new information.

2. **Document Key Topics**:
   - Assign a clear, descriptive title to each key topic that captures the core idea of the section.
   - Include the first two sentences from the section that introduces each topic. These sentences should signal a shift to a new theme or section, making it clear where the topic begins.

3. **Output Structure**:
   - Format the output as follows:
     **<Topic 1 Name>**
     <Two sentences marking the beginning of Key Topic 1>
     **<Topic 2 Name>**
     <Two sentences marking the beginning of Key Topic 2>

Please analyze the following document using above rules:
"""



prompt_prefix2= """
You will be given a key topic, its starting lines, the starting lines of the next topic (or "" if it's the last topic), and a complete document. Your task is to create slides based on the portion of the document between these starting lines. Follow these steps:

1. Identify the relevant section of the document between the given starting lines.
2. Analyze this section and create slides with titles and bullet points.

Your task is to create a set of PowerPoint slides based on the portion of the document that lies between the given starting lines. Follow these steps carefully:

You are a power point creating expert who creates great ppts by following the below instructions:
1. **Identify the Relevant Section**: Extract the section of the document that begins with the 'Starting Lines for This Topic' and ends just before the 'Starting Lines for Next Topic'.
2. **Analyze the Content**: Review this section thoroughly to understand the key points that need to be included in the slides.
3. **Slide Creation**:
   - The number of slides should be determined by the amount of unique, non-redundant information. This can range from 1 to 10 slides.
   - **Order**: Arrange the slides in the sequence that the information appears in the document.
   - **Bullet Points**:
     - Each slide should contain atmost 3 concise bullet points.
     - Give content of the bullet point as if you are an expert in PPT making, consise and clear.
     - Each bullet point must be a complete, meaningful sentence that clearly conveys key information.
     - Ensure each bullet point is concise, with as low number of  words as possible.
     - **Relevance**: If certain information is applicable to more than one topic, include it in the slides for the current key topic if it appears first in the document.
   - **Avoid Redundancy**: Ensure that there is no repetition of content across the slides for the same key topic.
Output Format:
**<title>**
* content
* content
* content
**<title>**
* content
* content
* content


Inputs:
Key Topic: '''{{keytopic}}'''
Starting Lines for This Topic: '''{{startingLines}}'''
Starting Lines for Next Topic : '''{{nextTopicStartingLines}}'''

Document:

{{pasteFullDoc}}


Please create slides based on the section of the document between the given starting lines, following the guidelines provided. Ensure that the slides comprehensively cover the key topic without unnecessary repetition.
"""