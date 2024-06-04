import xml.etree.ElementTree as xmletree
import os 

# 解析语言配置文件的XML内容，为后续处理配置信息做准备
ConfigXmlTree = xmletree.parse("../conf/config.xml")
ConfigRoot = ConfigXmlTree.getroot()

@staticmethod
def update_xml_config(file_path, root, new_language):
    # 检查并更新或插入语言配置
    config_element = None
    for element in root:
        if element.tag == "config" and element.get("value") == new_language:
            config_element = element
            break

    if config_element is None:
        config_element = xmletree.SubElement(root, "config")
        config_element.set("value", new_language)

    tree = xmletree.ElementTree(root)
    with open(file_path, "wb") as xml_file:
        tree.write(xml_file)

@staticmethod
def ChangeDefaultLanguage():
    DefaultLanguage = input("Please input the language you want to use: ")
    if DefaultLanguage == "CN":
        print("你已选择汉语作为你的默认语言。")
        DefaultLanguage = xmletree.SubElement(ConfigRoot,"config")
        DefaultLanguage.set("value","CN")
        tree = xmletree.ElementTree(ConfigRoot)
        tree.write("../conf/config.xml")
    elif DefaultLanguage == "EN":
        print("You have selected English as your default language.")
    else:
        print("You haven't selected a language yet.")
    return

if __name__ == "__main__":
    ChangeDefaultLanguage()