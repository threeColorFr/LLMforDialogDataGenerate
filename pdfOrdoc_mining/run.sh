#! /bin/bash
function read_dir(){
    echo $1
    echo $2
    for file in `ls $1`       #注意此处这是两个反引号，表示运行系统命令
    do
        if [ -d $1/$file ]  #注意此处之间一定要加上空格，否则会报错
        then
            mkdir -p $2/$file
            read_dir $1/$file $2/$file
        else
            #echo $1/$file   #在此处处理文件即可
            #echo $2/$file
            infile=$1/$file
            outfile=$2/$file

            suffix="${infile##*.}" # 文件名后缀
            
            if [ $suffix = "pdf" ]; then
                nohup python main_pdf.py $infile $outfile &
            elif [ $suffix = "docx" ]; then
                nohup python main_doc.py $infile $outfile &
            elif [ $suffix = "txt" ]; then
                cp $infile $outfile
            else
                echo "extra file type"
            fi
        fi
    done
}   
#读取第一个参数
read_dir $1 $2 # 输入的pdf文件夹；输出的txt文件夹

# bash run.sh ../Data2 ../Data2_txt