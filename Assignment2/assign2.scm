; Password for Submit: 16andcounting

(define (author)
    (println "AUTHOR: Kyle Galloway ckgalloway@crimson.ua.edu")
)

; (define (exprTest # $expr target)
;     (define result (catch (eval $expr #)))
;     (if (error? result)
;         (println $expr " is EXCEPTION: " (result'value)
;             " (it should be " target ")")
;         (println $expr " is " result
;             " (it should be " target ")")
;     )
; )

(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (println)
    (cond
        ((error? result)
            (println $expr " is EXCEPTION:")
            (println (result'value))
            (println "It should be:")
            (println target))
        (else
            (println $expr " is: ")
            (println result ", it should be: ")
            (println target)
        )
    )
)

; Task 1
(define (loop f L)
    ; If list is empty
    (if (null? L)
        ; Return null
        nil
        ; If the first part is less than the second part of the list
        (if (< (car L) (cadr L))
            (begin
                ; Call the function on the first part
                (f (car L))
                ; And recursively call loop on the rest of the sequence
                (loop f (list (+ (car L) 1) (cadr L)))
            )
        )
    )
)

; Task 2
(define (curry @)
    ; Checks if the arg is the function itself or if it is nested further down
    (if (is? (car @) 'CONS)
        ; If it is nested call the nested part L
        (define L (car @))
        ; Otherwise call the whole thing L
        (define L @)
    )
    ; Define need as the amount of parameters needed for the function in L
    (define (need) (length (get 'parameters (car L))))
    ; If length of cdr L (# of args) is less than needed
    (if (< (length (cdr L)) (need))
        ; Make a lambda that recalls the function with a more flattened list
        (lambda (@) (curry (append L @)))
        ; Else, apply the function to the rest of the list.
        (apply (car L) (cdr L))
    )
)

; Task 3
; Returns the top element of the stack
(define (peek S)
    (if (null? S)
        '()
        (car S)
    )
)
; Returns the stack without the top element
(define (pop S)
    (if (null? S)
        '()
        (cdr S)
    )
)
; Adds an element to the front of a S
(define (push S el)
    (if (null? S)
        (list el)
        (append (list el) S)
    )
)
; Returns true if op1 has higher precedence than op2
(define (checkPrec op1 op2)
    (define prList '(^ / * - +))
    (define (iter prList)
        (cond
            ((== (car prList) op1) #t)
            ((== (car prList) op2) #f)
            (else (iter (cdr prList)))
        )
    )
    (iter prList)
)
; Adds all of the given list to a stack (basically reverses it)
(define (pushAll L)
    (define (iter LL S)
        (if (null? LL)
            S
            (iter (cdr LL) (push S (car LL)))
        )
    )
    (iter L '())
)
; Makes an expression from the element and the top 2 items of the stack
(define (makeExpr S el)
    (append (list (list el (car S) (cadr S))) (cddr S))
)
; Empties the ops stack onto the output stack and returns the output
(define (emptyStack output ops)
    ; (println output " : " ops)
    (if (null? ops)
        output
        (if (>= (length ops) 2)
            (emptyStack (makeExpr output (car ops)) (cdr ops))
            (emptyStack (makeExpr output (car ops)) nil)
        )
    )
)

(define (infix->prefix Expr)
    (define (iter in out ops)
        ; (println in " : " out " : " ops)
        (if (null? in)
            (car (emptyStack out ops))
            (cond
                ((integer? (car in))
                    (iter (cdr in) (push out (car in)) ops)
                )
                ((symbol? (car in))
                    (if (null? ops)
                        (iter (cdr in) out (push ops (car in)))
                        (if (checkPrec (car in) (car ops))
                            (iter (cdr in) out (push ops (car in)))
                            (iter in (makeExpr out (car ops)) (cdr ops))
                        )
                    )
                )
            )
        )
    )
    (iter (pushAll Expr) nil nil)
)

; Task 4


; Task 5

(define (fix L)
    (define (fix ly)
        (if (not (null? ly))
            (if (integer? (car ly))
                ly
                (list (append (car ly) (fix (cdr ly))))
            )
            nil
        )
    )
    (fix L)
)

(define (convert Expr)
    (define (iter exp curr)
        (if (not (null? (cdr exp)))
            (iter (cdr exp) (append curr (list (list 'lambda (list (car exp))))))
            (append curr (list (list 'lambda (list (car exp)))))
        )
    )
    (car (fix (append (iter (cadr Expr) '()) (list (caddr Expr)))))
)

; Task 6
(define (replace-paren L)
    (define (replace-iter L newL)
        ; If L is a list
        (if (and (list? L) (not (null? L)))
            ; If (car L) is not a list
            (if (not (list? (car L)))
                ; Recur with L=>(cdr L) & newL=>(newL (car L))
                (replace-iter (cdr L)
                              (append newL (list (car L)))
                )
                ; Else, recur with L=>(cdr L) &
                ;     newL=>(newL (replace (car L)))
                (replace-iter (cdr L) (append newL (replace-paren (car L))))
            )
            ; Else, return (newL 'r)
            (append newL (list 'r))
        )
    )
    ; Call replace-iter with L and ('l)
    (replace-iter L (list 'l))
)

(define (rewrite L)
    (define (rewrite-iter L newL)
        (if (and (list? L) (not (null? L)))
            (cond
                ; If (car L) is 'l make newL a list
                ; Cool function that inserts deep needs to go here
                ((== (car L) 'l) (rewrite-iter (cdr L) (list newL)))
                ; If (car L) is an integer (append newL (list (car L)))
                ((integer? (car L))
                    (rewrite-iter (cdr L) (append (list (car L)) newL))
                )
                ; Else, make newL a list
                (#t (rewrite-iter (cdr L) (cons '() newL)))
            )
            newL
        )
    )
    (car (rewrite-iter L '()))
)

(define (reverse* L)
    ; (replace-paren L)
    (rewrite (replace-paren L))
)

; Task 7
; Same as in book
(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence)
            (accumulate op initial (cdr sequence))
        )
    )
)
; Same as in book
(define (accumulate-n op init seqs)
    (if (null? (car seqs))
        nil
        (cons (accumulate op init (map car seqs))
              (accumulate-n op init (map cdr seqs))
        )
    )
)
; Same as in book
(define (transpose mat)
    (accumulate-n cons nil mat)
)
; Same as in book
(define (dot-product v w)
    (accumulate + 0 (map * v w))
)
; Same as in book but transpose the matrix at the beginning
(define (matrix-*-vector m v)
    (map (lambda (row) (dot-product row v)) (transpose m))
)
; Same as in book but don't transpose the matrix at the beginning
(define (matrix-*-matrix m n)
    (map (lambda (row) (matrix-*-vector n row)) m)
)


; Task 8
(define (node value left right)
    (define (display) (print value))
    this
)

(define (displayTree root indent)
    (if (valid? root)
        (begin
            (displayTree (root'right) (string+ indent "    "))
            (print indent)
            ((root'display))
            (println)
            (displayTree (root'left) (string+ indent "    "))
        )
    )
)

(define (insertInTree root item)
    (if (>= item root'value)
        (if (null? root'right)
            ; (define (root'right) (node item nil nil))
            ; (insertInTree root'right item)
        )
        (if (null? root'left)
            ; (define (root'left) (node item nil nil))
            ; (insertInTree root'left item)
        )
    )
)

; Task 9
(define (big+ a b)
    (define (iter a b total addin)
        (println "a: " a " :b: " b " :total: " total " :addin: " addin)
        (if (> (length a) 0)
            (if (> (length b) 0)
                (begin
                    (define s (+ (car a) (car b) addin))
                    (if (> s 9)
                        (if (> (length total) 0)
                            (iter (cdr a) (cdr b) (append total (list (- s 10))) 1)
                            (iter (cdr a) (cdr b) (list (- s 10)) 1)
                        )
                        (if (> (length total) 0)
                            (iter (cdr a) (cdr b) (append total (list s)) 0)
                            (iter (cdr a) (cdr b) (list s) 0)
                        )
                    )
                )
                (if (> (length total) 0)
                    (append total a)
                    a
                )
            )
            (if (> (length b) 0)
                (if (> (length total) 0)
                    (append total b)
                    b
                )
                total
            )
        )
    )
    (if (== '- (car a))
        (if (== '- (car b))
            (reverse (iter (reverse (car a)) (reverse (car b)) nil 0))
            (reverse (append (iter (reverse (car a)) (reverse b) nil 0)) '-)
        )
        (if (== '- (car b))
            (reverse (append (iter (reverse a) (reverse (car b)) nil 0)) '-)
            (reverse (iter (reverse a) (reverse b) nil 0))
        )
    )
)

(define (big- a b)
    (if(== (car b) '-)
        (big+ a (cdr b))
        (big+ a (append '(-) b))
    )
)

(define (big* a b))

; Task 10


; Tests
(define (run1)
    (loop (lambda (x) (inspect x)) '(0 5))
    (loop (lambda (x) (println (* x x))) '(1 11))
    (loop (lambda (x) (println (+ x x x))) '(1 11))
    (loop (lambda (x) (println (sqrt x))) '(1 10))
)

(define (plus a b c d e)
      (+ a b c d e)
)
(define (run2)
    (inspect (curry plus 1 2 3 4 5))
    (inspect ((curry plus 1) 2 3 4 5))
    (inspect ((curry plus 1 2) 3 4 5))
    (inspect ((curry plus 1 2 3) 4 5))
    (inspect ((curry plus 1 2 3 4) 5))
    (inspect (((curry plus 1) 2) 3 4 5))
    (inspect (((curry plus 1) 2 3) 4 5))
    (inspect (((curry plus 1) 2 3 4) 5))
    (inspect (((((curry plus 1) 2) 3) 4) 5))
)

(define (run3)
    (inspect (eval (infix->prefix '(1 * 2 + 3)) this))
    (inspect (eval (infix->prefix '(1 + 2 * 3)) this))
    (inspect (eval (infix->prefix '(1 - 2 * 3)) this))
    (inspect (eval (infix->prefix '(1 - 2 * 3 + 4)) this))
    (inspect (eval (infix->prefix '(1 + 2 * 3 + 4)) this))
    (inspect (eval (infix->prefix '(1 + 1)) this))
)

; (define (run4))

(define (run5)
    (println (convert (quote (lambda (a b) (+ a b)))))
    (println (convert (quote (lambda (a b c) (+ a b c)))))
    (println (convert (quote (lambda (a b c d) (+ a b c d)))))
)

; (define (run6)
;     (inspect (reverse* (list 1 (list 2 (list 3  (list 4 5))))))
;     (inspect (reverse* (list 1 2 3 (list 4 5))))
;     (inspect (reverse* (list 1 (list 2 3) (list 4 5))))
;     (inspect (reverse* '(1 2 3 4 5)))
; )

(define (run7)
    (define v1 '(1 2 3))
    (define w1 '(4 5 6))
    (define m1 '((1 4) (2 5) (3 6)))
    (define m2 '((1 2 3) (2 3 4) (3 4 5) (4 5 6)))
    (define m3 '((10 10) (10 10) (10 10)))
    (define m4 '((1 4 6) (2 5 7) (3 6 8) (4 7 9)))
    (define m5 '((4 6 9 1) (3 6 8 4) (2 5 7 6)))
    (define m6 '((1 2 3)(10 20 30)(100 200 300)))
    (define I3 '((1 0 0) (0 1 0) (0 0 1)))
    (exprTest (dot-product v1 w1) 32)
    (exprTest (matrix-*-vector m1 v1) '(14 32))
    (exprTest (matrix-*-matrix m2 m3) '((60 60) (90 90) (120 120) (150 150)))
    (exprTest (matrix-*-matrix m4 m5) '((28 60 83 53) (37 77 107 64) (46 94 131 75) (55 111 155 86)))
    (exprTest (matrix-*-matrix m5 m4) '((47 107 147) (55 118 160) (57 117 157)))
    (exprTest (matrix-*-matrix m6 I3) '((1 2 3)(10 20 30)(100 200 300)))
    (exprTest (dot-product '(0) '(0)) 0)
    (exprTest (transpose '((0))) '((0)))
    (exprTest (matrix-*-vector '((0)) '(0)) '(0))
    (exprTest (matrix-*-matrix '((0)) '((0))) '((0)))
)

; (define (run8)
;     (define t0 (node 5 nil nil))
;     (define t1 (insertInTree t0 2))
;     (define t2 (insertInTree t1 8))
;     (displayTree t2 "   ")
; )

(define (run9)
    (exprTest (big+ '(1 1 1 1) '(1 1 1 1)) '(2 2 2 2))
    (exprTest (big+ '(- 1 1 1 1) '(1 1 1 1)) '(0 0 0 0))
    (exprTest (big+ '(1 1 1 1) '(- 1 1 1 1)) '(0 0 0 0))
    (exprTest (big+ '(- 1 1 1 1) '(- 1 1 1 1)) '(- 2 2 2 2))
    (exprTest (big+ '(4 5 8 9) '(3 0 2)) '(4 8 9 1))
    (exprTest (big+ '(3 0 2) '(4 5 8 9)) '(4 8 9 1))
    (exprTest (big- '(1 1 1 1) '(1 1 1 1)) '(0 0 0 0))
    (exprTest (big- '(- 1 1 1 1) '(1 1 1 1)) '(- 2 2 2 2))
    (exprTest (big- '(1 1 1 1) '(- 1 1 1 1)) '(2 2 2 2))
    (exprTest (big- '(- 1 1 1 1) '(- 1 1 1 1)) '(0 0 0 0))
    (exprTest (big- '(1 1 1 1) '(1 1 1)) '(1 0 0 0))
    (exprTest (big- '(1 0 0) '(1 1 0 0)) '(- 1 0 0 0))
)

; (define (run10))

; Run tests
; DONE (run1)
; DONE (run2)
; DONE (run3)
; (run4)
; DONE (run5)
; (run6)
; DONE (run7)
; (run8)
(run9)
; (run10)
(println "assignment 1 loaded!")
