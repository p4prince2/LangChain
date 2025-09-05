from langchain_community.tools import ShellTool

shelltool=ShellTool()

result=shelltool.invoke('ls')

print(result)