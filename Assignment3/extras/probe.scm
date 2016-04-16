(define (probe q w name)
    (define (action)
        (define delay 1)
        ((get 'insert q) delay
                        (lambda ()
                            (println ((get 'peekTime q)) ": wire " name " has a new value: " ((get 'get w)))
                        )
        )
    )

    ((get 'add w) action)
)