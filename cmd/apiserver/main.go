package main

import (
	"github.com/goriiin/dp-serv/internal/app/apiserver"
	"log"
)

func main() {
	config := apiserver.NewConfig()
	s := apiserver.New(config)
	if err := s.Start(); err != nil {
		log.Fatal(err)
	}

}
