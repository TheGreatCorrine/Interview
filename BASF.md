### Why are you interested in working in BASF
Team culture, company culture很好


## OpenText Documentum
1. 一句话形容这是什么
   enterprise-grade content management 帮助企业高效管理文档
   OpenText Documentum 是一个现成的软件，但是就像别的手机在ios系统上装软件一样，我们也需要去customize这个documentum
3. 主要components
   - content server
   - d2(web frontend)
   - D2 config工具
4. How to monitor a workflow in OpenText __D2__
  - 这个workflow不是开发流程，而是指文档审批，处理，归档一系列流程，一组自动化的流程，比如文档先发给谁审批，然后再发给谁，最后归档，伴随approve，reject，reassign等状态
    a predefined, automated sequence of steps that a document must go through, all actions are traceable for compliance purposes
  - How to initiate a workflow?
    General - Performers - Documents - Schedule
  - How to track the progress of a workflow?
5. 可能会customize的地方
  - 新建定制的文档类型（Document Type）
    比如BASF特有的「产品安全报告」、「全球法规合规文件」
  - 定制审批流程（Workflow）
    比如不同国家的合同审批链条不同（中国→法务→财务 / 德国→直接财务）
  - 开发自定义按钮、插件、脚本
    比如上传按钮旁边多加一个「加急审批」按钮 比如审批超时72小时自动提醒功能（写个小Java module）
  - 定制前端界面（D2 Client）
    调整表单顺序、默认显示列、增加快速搜索栏
  - 写数据库查询、小脚本支持业务
    比如一键生成一周未审批文档列表



## Interview Prep
1. Project (English)
   RPM 精准把握用户需求 因为自己是深度用户 从而争取到了这个机会 后面通过主动的沟通（举个例子） 弄清了bachir不清楚的需求
   HRM 类似医药行业 但相关性不大❌
   提一嘴自己对Documentum也有所了解，做过一些course project，并且专门看了opentext documentum的官方视频
