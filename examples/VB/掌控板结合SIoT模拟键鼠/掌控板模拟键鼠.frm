VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   3030
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   4560
   LinkTopic       =   "Form1"
   ScaleHeight     =   3030
   ScaleWidth      =   4560
   StartUpPosition =   3  '����ȱʡ
   Begin VB.CommandButton Command2 
      Caption         =   "�˳�"
      Height          =   735
      Left            =   1440
      TabIndex        =   1
      Top             =   1440
      Width           =   1815
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   200
      Left            =   600
      Top             =   2160
   End
   Begin VB.CommandButton Command1 
      Caption         =   "��ʼ"
      Height          =   735
      Left            =   1440
      TabIndex        =   0
      Top             =   360
      Width           =   1815
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Declare Function SetCursorPos Lib "user32" (ByVal x As Long, ByVal y As Long) As Long
Private Declare Sub mouse_event Lib "user32" (ByVal dwFlags As Long, ByVal dx As Long, ByVal dy As Long, ByVal cButtons As Long, ByVal dwExtraInfo As Long)
Private Const MOUSEEVENTF_LEFTDOWN = &H2
Private Const MOUSEEVENTF_LEFTUP = &H4


Private Sub Command1_Click()
    Timer1.Enabled = True
End Sub

Private Sub Command2_Click()
    End
End Sub

Private Sub Timer1_Timer()
    Dim strUrl As String
    Dim responseStr As String
    Dim search1, search2, pos1, pos2, searchID1, searchID2, posID1, posID2
    Dim msg, ID As String
    Dim mykey
    search1 = "Content"
    search2 = "Created"
    searchID1 = "ID"
    searchID2 = "Topic"
      

    Rem Set XMLObject = CreateObject("Microsoft.XMLHTTP")  ʧ��
    Set xmlobject = CreateObject("MSXML2.ServerXMLHTTP")       ' �ɹ�
    strUrl = "http://192.168.100.7:8080/lastmessage?topic=DFRobot/mouseandkeyborad&iname=siot&ipwd=dfrobot" '���������
    xmlobject.open "GET", strUrl, False
    xmlobject.send
    If xmlobject.ReadyState = 4 Then
        responseStr = xmlobject.responseText    '���������ص�JSON���� ����{"code":1,"data":[{"ID":102,"Topic":"DFRobot/mouseandkeyborad","Content":"I am from siot","Created":"2020-02-16 18:03:13"}],"msg":"�ɹ�"}   ����ˣ���Ҫ��ȡ
        pos1 = InStr(1, responseStr, search1, 1)    '
        pos2 = InStr(1, responseStr, search2, 1)
        msg = Mid(responseStr, pos1 + 10, pos2 - 3 - pos1 - 10)     '��ȡ��ȡsiot����Ϣmsg
        
        posID1 = InStr(1, responseStr, searchID1, 1)
        posID2 = InStr(1, responseStr, searchID2, 1)
        ID = Mid(responseStr, posID1 + 4, posID2 - 3 - posID1 - 3)
        If ID <> IDpre Then       'Ϊ�˷�ֹ���󵽵���Ϣ����ͬһ����Ϣ����Ҫ�Ա���ϢID��IDpre��ȫ�ֱ���
            IDpre = ID
            Rem ����siot���ص���Ϣ��ģ�����������
            'SetCursorPos 335, 181 '������Ըĳ����λ��
            'mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 '��갴��
            'mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 '��굯��
            
            Rem ���̲���
            If msg = "LEFT" Then
                SendKeys "{LEFT}"
            ElseIf msg = "RIGHT" Then
                SendKeys "{RIGHT}"
            ElseIf msg = "UP" Then
                SendKeys "{UP}"
            ElseIf msg = "DOWN" Then
                SendKeys "{DOWN}"
            ElseIf msg = "F5" Then
                SendKeys "{F5}"
            ElseIf msg = "ESC" Then
                SendKeys "{ESC}"
            ElseIf msg = "ENTER" Then
                SendKeys "{ENTER}"
            End If
            
        End If
        
        

    End If
    Set xmlobject = Nothing

End Sub

























