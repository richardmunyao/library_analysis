import pandas as pd
from library_app.models import BookInfo


def handle_uploaded_file(f):
    csvfile = f
    dataframe = pd.read_csv(f)
    # print(dataframe)

    # v here stands for value.
    # my goodness, this is horrible. Find a better way
    v_goodr_ids = dataframe['Book Id'].values
    v_titles = dataframe['Title'].values
    v_authors = dataframe['Author'].values
    v_isbns = dataframe['ISBN'].values
    v_my_ratings = dataframe['My Rating'].values
    v_avg_ratings = dataframe['Average Rating'].values
    v_pages = dataframe['Number of Pages'].values
    v_date_addeds = dataframe['Date Added'].values
    v_shelfs = dataframe['Exclusive Shelf'].values


    for title, author in zip(v_titles,v_authors):
        print(title,"=>",author)

    print("First title:",v_titles[0])

    #create instances of book info, make entries.
    #Surely there's a better way of doing this!
    for i in range(len(dataframe)):
        print("TITLES I:",v_titles[i])
        i = BookInfo(
        goodr_id=v_goodr_ids[i],
        title=v_titles[i],
        author=v_authors[i],
        isbn=v_isbns[i],
        my_rating=v_my_ratings[i],
        avg_rating=v_avg_ratings[i],
        pages=v_pages[i],
        date_added=v_date_addeds[i],
        shelf=v_shelfs[i]
        )
        i.save()

    print('*************************************')
    print("All objects: ")
    all_entries = BookInfo.objects.all()
    print(all_entries.values('title'))
