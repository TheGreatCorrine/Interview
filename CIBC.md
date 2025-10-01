"""
Discuss your programming experience

Do you have experience with Pandas

Natural Language Processing
"""

今天cibc面试问了三个问题，一个是为什么apply，这个答得还可以
还有一个是walk me through your resumes and cover letters，这个问题我无法控制好时长，下次可以让他们先clarify一下要答多久，大概组织一下语言-包含几点bullet points，每个怎么通过细节展示；同时不要太依靠template和读答案，更多是背答案临时组织控制好时长
最后一个怎么给non-technical的人解释一些概念，这是个很常见的bq，好好准备
比较特殊的一个点是这个hr生病了，下次要多一点人文关怀
还有就是对hr少聊一点技术细节，多展现你个人interpersonal skills，今天这个策略不对，聊的技术细节太多了

0. Greetings
   Hi Allison,
   how are you doing today?
   I'm doing great thank you. it’s so good to see you again!
   (可以放最后)We actually connected last term when I applied for this role, but due to a family emergency I couldn’t join. I’m really glad to have the chance to reconnect today.

2. **Why did you apply to this role?**

   [Shorter]I applied because CIBC is one of Canada’s leading banks that values innovation, client experience, and people. I also had a very positive impression from my last application process, which showed me how supportive the work environment is.
   And Specifically, ...
   
   
   **[Equivalent] Why are you interested in working at CIBC?**
   1. Canada's leading banks that values innovation, client experience, and people.
   2. I appreciate that CIBC invests in its employees and creates strong career growth opportunities. During my last application process, I felt very supported, (I was very happy when I received the offer call, but unluckily, I couldn't join due to family emergencies)
      But that experience gave me a sense that the work environment would be equally positive.
   3. On a personal note, I’m also a CIBC client, and I’ve always had a positive impression of how the bank treats its customers.
      Altogether, I see CIBC as a place where I can contribute meaningfully, and grow both technically and professionally.
   
   **Why are you interested in this role particularly?**
   1. For this role specifically, I think it’s a great fit for my unique background.
   2. The posting mentioned Enterprise Technology and Business Management — and I bring both: I started in business at Rotman before fully focusing on computer science.
   3. That means I not only have strong technical skills, but I also understand client needs and business logic better than most developers.
   4. I see CIBC as the perfect platform to further polish my technical skills in a well-structured organization, and hopefully contribute to projects that can impact millions of people.

   4. [This unique blend(combination of Enterprise Technology and Business Management) really attracts me. Hope to work on interesting and meaningful projects]
   
   
5. Tell me about yourself.
   [Equivalent] Walk me through your resume.

   1. Background:
      Of course! Just to give you a quick overview, I actually have a blended background in both business and computer science. I started my studies in Rotman Commerce, and gained a strong foundation in business. I also polished my people skills at Rotman. Later I transitioned into Computer Science because I wanted to focus more on the technology side. I see the growing potentials of GenAI and how it can change people's lives. Along the way, I've done well academically, (I think you can see that from my transcript). But more importantly, I really enjoy applying my knowledge to real-world projects and building meaningful softwares.

   2. Project/Internship: For example, I recently worked as an AI intern at BSH, where I helped develop a food freshness detection system on Raspberry Pi devices. I helped deploy the Python model. I also built a prototype. It was an intelligent refrigerator testing data monitor system, which saved test engineers one hour a day. 
      Re:Pair Genomics: the internal Human Resources Management. I proposed a serverless architecture for the system. This solution made the system scalable, and also cut the infrastructure costs by over $100 per employee per month.
      I was also working part-time at the Rotman School of Management and helped them maintain their trading apps. That's an evidence of combining tech and business.

   3. Conclusion: Overall, I bring strong 


BQ   
1. How do you explain some concepts to people with non-technical backgrounds? (她问这个问题应该是随机的）
   Absolutely, when it comes to explaining:
   I really focus on two things:
   1. I put myself in their shoes - understand their domain, what they care about, so I can speak their language.
   2. I tailor the information to what they need to know
      For users, that might mean a simple user guide on how to use the app.
      For managers, a clear project timeline. 
      For colleagues, I might use an analogy to make it relatable
   I adapted my communication style
2. The challenge you met during internship?
   Sure. One of my the challenge I met
   1. Translate non-technical stakeholder Speak their language
   2. Understand client needs
     figuring out exactly what the clients wanted because their needs change almost every week.
      For example, in the first week, they told me they wanted an Ai agent that can analyze testing data from historal records
      Then the very next week, they said they wanted a real-time monitoring
      And after that, they decided they no longer need theed user authentication anymore, so I had to refactor the whole backend.      
   They were not sure what they wanted - so ambuguities
   To manage all the changes, I gathered everyone together and asked them to set a deadline for finalizing thier needs. We agreed to have frequent meetings before that deadline to clarify everything and after that day passed, they commited to only make small changes.
   After the ddl, initial version of what they described, showed it to them, and let them confirm if it was what they had in mind
   I adjust the solution step by step and wrote documentations.
   After clarifying everything, the development itself was not that hard. It was really about narrowing down the business needs and the demo was successful.
3. Deal with a difficult team member
   Sure. A different
4. High stress
5. Adaptability (similar to high stress)


1. BSH FFD
   - involves a refrigerator setup, where we placed a Raspberry Pi and a camera. There were also sensor data collectors. When you open the drawer and put some food inside, it starts capturing images and analyzing the data. I mainly work with Python to update backend code. Since you could replace chips, I ended up developing different features on different devices.
   - Reboot：original solution - we had an external executable for one of the sensor collectors that the main Python script couldn't directly control. Essentially, the sensor process would continue running indefinitely and wouldn't terminate with the rest of the code.
     The old approach - reboot the whole Raspberry Pi to reset everything. downtime. offset.
     a system service
2. BSH Smart Monitor
   - application developed for refrigerator testing engineers to monitor testing data in real-time
   - 
   - architecture (prototype + ai integration
4. HRM:
   - a light-weight HRM portal focused on payroll; a portal for their employees to manage their accounts and receive their pay automatically (ADP)
   - The client was a startup with small number of users 1. keep costs down 2. easy to maintain 3. low-volume
   - Why serverless 
