# 说明
- 需要从https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe下载excel文件并保存到当前文件夹文件 **Hotel_Reviews.csv** 中
- 文件太大了，不放到git里面

# Data Content

## 通用字段
- Average_Score: (平均得分，根据去年的最新评论计算得出，后面可以根据具体每一次得分再算出一个平均值，两相对比)
- Hotel_Name: 酒店名
- Reviewer_Nationality: 哪个国家的评论者(由于民族倾向，某些国籍更有可能给出正面或负面评价)
- Total_Number_of_Reviews: 这家酒店的评论数，后面可以根据具体评论再算出一个值，两相对比
- Additional_Number_of_Scoring: 给出评论分数，但评论者未撰写正面或负面评论


## 评论相关字段
- Reviewer_Score: 用户每一次具体的打分，最小值和最大值 2.5 和 10 之间最多保留 1 位小数的数值
- Negative_Review: 负面评论。如果什么也没写，该字段将显示 “No Negative”
- Review_Total_Negative_Word_Counts: 负面评论字数（负面字数越高表示得分越低）.
- Positive_Review: 正面评论。如果什么也没写，该字段将显示 “No Positive
- Review_Total_Positive_Word_Counts: 正面评论字数（正面字数越高表示得分越高）.

## 时间相关
- days_since_review: Duration between the review date and scrape date.
- Review_Date: Date when reviewer posted the corresponding review.

## 审稿人专栏
- Total_Number_of_Reviews_Reviewer_Has_Given: Number of Reviews the reviewers has given in the past.

## 其他字段
- Tags: Tags reviewer gave the hotel.
- lat: Latitude of the hotel
- lng: longtitude of the hotel
- Hotel_Address: Address of hotel.














