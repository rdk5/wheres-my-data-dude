Sub bookCleaning()
    Dim tweetText As String
    Dim statusID As String
    Dim lastRow As Double

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow

        tweetText = Cells(i, 4).Value
        statusID = Cells(i, 5).Value
        If IsNumeric(statusID) = True Then
        ElseIf IsNumeric(Cells(i, 6).Value) = True Then
            Cells(i, 4).Value = tweetText + statusID
            Cells(i, 5).Value = Cells(i, 6).Value
            Cells(i, 6).Value = Cells(i, 7).Value
            Cells(i, 7).Value = ""
        ElseIf IsNumeric(Cells(i, 7).Value) = True Then
            Cells(i, 4).Value = tweetText + statusID + Cells(i, 6).Value
            Cells(i, 5).Value = Cells(i, 7).Value
            Cells(i, 6).Value = Cells(i, 8).Value
            Cells(i, 7).Value = ""                
            Cells(i, 8).Value = ""
        ElseIf IsNumeric(Cells(i, 8).Value) = True Then
            Cells(i, 4).Value = tweetText + statusID + Cells(i, 6).Value + Cells(i, 7).Value
            Cells(i, 5).Value = Cells(i, 8).Value
            Cells(i, 6).Value = Cells(i, 9).Value
            Cells(i, 7).Value = ""
            Cells(i, 8).Value = ""
            Cells(i, 9).Value = ""
        ElseIf IsNumeric(Cells(i, 9).Value) = True Then
            Cells(i, 4).Value = tweetText + statusID + Cells(i, 6).Value + Cells(i, 7).Value + Cells(i, 8).Value
            Cells(i, 5).Value = Cells(i, 9).Value
            Cells(i, 6).Value = Cells(i, 10).Value
            Cells(i, 7).Value = ""
            Cells(i, 8).Value = ""
            Cells(i, 9).Value = ""
            Cells(i, 10).Value = ""
        ElseIf IsNumeric(Cells(i, 10).Value) = True Then
            Cells(i, 4).Value = tweetText + statusID + Cells(i, 6).Value + Cells(i, 7).Value + Cells(i, 8).Value + Cells(i, 9).Value
            Cells(i, 5).Value = Cells(i, 10).Value
            Cells(i, 6).Value = Cells(i, 11).Value
            Cells(i, 7).Value = ""
            Cells(i, 8).Value = ""
            Cells(i, 9).Value = ""
            Cells(i, 10).Value = ""
            Cells(i, 11).Value = ""
        End If
    Next i
End Sub

