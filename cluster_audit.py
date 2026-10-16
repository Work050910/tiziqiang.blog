import re
import os

# Audit intent clusters
clusters = [
    {
        "cluster_name": "簇 A：退款条款与维权边界",
        "posts": [
            ("/good-ladder/post-11/", "好用的梯子服务条款怎么读？退款与服务边界解析"),
            ("/ladder-guide/post-06/", "翻墙梯子退款机制全景：购买前必须理清的售后边界"),
            ("/ladder-tools/post-11/", "梯子工具退款争议应对：工单沟通技巧与记录留存")
        ],
        "overlap_issue": "三篇文章的核心意图均指向'退款维权'。其中 post-11 (good-ladder) 讲条款审查，post-06 (ladder-guide) 讲退款门槛全景，post-11 (ladder-tools) 讲工单沟通争议处置。目前存在'PayPal争议、不可抗力免责'等泛用论述重叠。",
        "remedy": "差异化分工：\n- good-ladder/post-11 专门聚焦【ToS 条款文本逐行解读与法律陷阱识别（审计规则、BT禁止项、不可抗力）】；\n- ladder-guide/post-06 专门聚焦【主流服务商实际公开退款条件矩阵（各平台小时数、流量阈值、扣手续费真实门槛）】；\n- ladder-tools/post-11 专门聚焦【实战故障工单撰写指南（如何提供 traceroute/ping/错误日志证据）与支付渠道申诉具体步骤】。"
    },
    {
        "cluster_name": "簇 B：购买前核验与避坑清单",
        "posts": [
            ("/good-ladder/post-01/", "好用的梯子怎么选？先核对套餐、流量和服务规则"),
            ("/ladder-guide/post-02/", "翻墙梯子推荐买前确认什么？四大核心指标检查表"),
            ("/how-to-choose/post-03/", "低预算梯子推荐注意什么？五大踩坑雷区预警"),
            ("/service/post-05/", "梯子服务购买前须知：消费者权益与自我保护意识")
        ],
        "overlap_issue": "四篇文章均出现'下单前检查清单'，反复提及'月付测试、重置日、倍率、优惠码'。",
        "remedy": "严格按标题分工：\n- good-ladder/post-01：建立【基础服务规则模型：自然月 vs 账单日计算表、高倍率损耗表】；\n- ladder-guide/post-02：建立【买前 5 分钟速查检查表（专注购买结算单页面的字段核验）】；\n- how-to-choose/post-03：专门揭露【低价黑产骗局（终身套餐资金盘、流氓客户端、虚标超售）】；\n- service/post-05：专门针对【个人隐私防护（支付账号隔离、避免真实身份泄漏、杜绝二手账号合租）】。"
    },
    {
        "cluster_name": "簇 C：月付与年付决策风险",
        "posts": [
            ("/good-ladder/post-03/", "好用的梯子套餐怎么比较？月付与年付的风险防范"),
            ("/how-to-choose/post-09/", "梯子月付与年付深度权衡：用风险收益模型做科学决策"),
            ("/ladder-tools/post-09/", "梯子工具轻量年付小包深度剖析：低预算用户的双刃剑")
        ],
        "overlap_issue": "均在阐述'年付有跑路风险、月付止损'的核心观点。",
        "remedy": "差异化分工：\n- good-ladder/post-03：横向对比【不同周期名义折扣与实付单价核算】；\n- how-to-choose/post-09：使用【数学期望公式与存续概率模型】进行金融学决策树推导；\n- ladder-tools/post-09：专门针对【百元以内轻量年付小包（30-50G/月）的特殊 QoS 限制与使用边界】。"
    },
    {
        "cluster_name": "簇 D：节点超时与故障排除",
        "posts": [
            ("/good-ladder/post-12/", "好用的梯子节点超时怎么排查？本地网络与节点状态分析"),
            ("/ladder-tools/post-08/", "梯子工具遇到节点批量超时怎么办？三分钟快速排查法")
        ],
        "overlap_issue": "两篇均讲解'四步排查法、时间同步、重启内核'，内容高度雷同。",
        "remedy": "差异化重写：\n- good-ladder/post-12：聚焦【系统层网络与 DNS 状态诊断（NTP 时间偏差、系统代理注册表、TUN 虚拟网卡驱动）】；\n- ladder-tools/post-08：聚焦【客户端核心运行时故障与端口冲突（7890 端口占用排查、内核崩溃日志查看、配置语法错误识别）】。"
    },
    {
        "cluster_name": "簇 E：多设备与并发",
        "posts": [
            ("/good-ladder/post-06/", "好用的梯子多设备并发限制：家庭与团队选型须知"),
            ("/how-to-choose/post-08/", "多设备协同选型：手机平板电脑路由器如何一套搞定")
        ],
        "overlap_issue": "均在谈'设备数与在线 IP 区别、软路由部署'。",
        "remedy": "差异化重写：\n- good-ladder/post-06：聚焦【服务商后台并发判定机制（IP 限制 vs 客户端指纹限制、FUP 触发条件）】；\n- how-to-choose/post-08：聚焦【跨平台客户端与路由器混合网络拓扑（旁路由网关科学分流 + 移动端漫游配置方案）】。"
    }
]

print("Cluster Audit Complete. Identified 5 major overlapping clusters.")
for c in clusters:
    print(f"\n{c['cluster_name']}")
    for p in c['posts']:
        print(f"  - {p[0]}: {p[1]}")
    print(f"  [处理建议]:\n  {c['remedy']}")
