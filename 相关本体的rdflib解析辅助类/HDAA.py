from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef

class HDAA(DefinedNamespace):
    """
    HDAA(Historical Data, Annotation, Association)类。
    """
    _NS = Namespace("http://purl.org/lmjxt/hdaa#")
    
    op_GL_ShiLiao : URIRef
    """ 关联史料 """
    op_GL_TianXiangJiLu : URIRef
    """ 关联天象记录 """
    op_GL_XueZhe : URIRef
    """ 关联学者 """
    op_GL_ZhuJie : URIRef
    """ 关联注解 """
    op_GuanLian : URIRef
    """ 关联关系 """
    op_JiSuanGuoCheng : URIRef
    """ 计算过程 """
    op_JiaoKanShiTi : URIRef
    """ 校勘实体 """
    op_ShuYuLaiYuan : URIRef
    """ 术语来源 """
    op_ShuZhiYuanSu : URIRef
    """ 数值元素 """
    op_ShuZhiZhuTiLeiXing : URIRef
    """ 数值主题类型 """
    op_ZhenShiQingKuang : URIRef
    """ 真实情况 """
    op_ZhenShiQingKuangJieGuo : URIRef
    """ 真实情况结果 """
    op_ZhuJieMuBiao_obj : URIRef
    """ 注解目标对象 """
    dp_XinShuZhi : URIRef
    """ 新数值 """
    dp_YuanShuZhi : URIRef
    """ 原数值 """
    dp_ZSQK_LiFaTuiSuan : URIRef
    """ 历法推算情况 """
    dp_ZSQK_ShiJi : URIRef
    """ 实际情况 """
    dp_ZSQK_ShiLiaoJiZai : URIRef
    """ 史料记载情况 """
    dp_ZhenWeiQingKuang : URIRef
    """ 真伪情况 """
    dp_ZhuJieMuBiao_text : URIRef
    """ 注解目标文本 """
    c_GLMS_ShiLiaoTianXiangJiLuZhuJieXueZhe : URIRef
    """ 史料—天象记录—注解—学者 """
    c_GuanLianMoShi : URIRef
    """ 关联模式 """
    c_ShuZhiYuanSu : URIRef
    """ 数值元素 """
    c_ShuZhiZhuTiLeiXing : URIRef
    """ 数值主题类型 """
    c_ZJST_ShuYuJieShi : URIRef
    """ 术语解释注解实体 """
    c_ZJST_ShuZhiJiSuanYuZhuanHuan : URIRef
    """ 数值计算与转换注解实体 """
    c_ZJST_WenZiKaoZheng : URIRef
    """ 文字考证注解实体 """
    c_ZJST_ZhenWeiKaoZheng : URIRef
    """ 真伪考证注解实体 """
    c_ZhenShiQingKuang : URIRef
    """ 真实情况 """
    c_ZhenShiQingKuangJieGuo : URIRef
    """ 真实情况结果 """
    c_ZhuJieShiTi : URIRef
    """ 注解实体 """
    i_SZZTLX_length : URIRef
    """ 长度数值类型 """
    i_SZZTLX_position : URIRef
    """ 方位数值类型 """
    i_SZZTLX_time : URIRef
    """ 时间数值类型 """
    i_ZSQKJG_1 : URIRef
    """ 记载正确 """
    i_ZSQKJG_2 : URIRef
    """ 记载错误或当时有意为之 """
    i_ZSQKJG_3 : URIRef
    """ 观测记录 """
    i_ZSQKJG_4 : URIRef
    """ 历推记录 """
    i_ZSQKJG_5 : URIRef
    """ 记载遗漏或当时有意为之 """
    i_ZSQKJG_6 : URIRef
    """ 历推结果不记录 """
    i_ZSQKJG_7 : URIRef
    """ 观测结果不记录 """