这里存放原始的pdf或者docx文件
支持多级目录

如果目录里有 `doc`文件，可以在wps中使用js宏批量转`doc -> docx`:

```
function docChangedocx() {
    var myDialog = Application.FileDialog(msoFileDialogFilePicker);
    myDialog.Filters.Clear();
    myDialog.Filters.Add("所有 WORD97-2003 文件", "*.doc", 1);
    myDialog.AllowMultiSelect = true;
    myDialog.Show();

    for (var i = 1; i <= myDialog.SelectedItems.Count; i++) {
        var file = myDialog.SelectedItems(i);
        var newFile = file.replace("doc", "docx");
        var doc = Documents.Open(file);
        doc.SaveAs(newFile, 12);
        doc.Close();
    }
}

```
