                +----------------+
                |    main.py     |
                +-------+--------+
                        |
                        v
               +-----------------+
               | report_builder  |
               +--------+--------+
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
     rss.py         reader.py     summarizer.py
        |               |               |
        +---------------+---------------+
                        |
                        v
                 DailyReport Model
                        |
                        v
             (future) Markdown Renderer
