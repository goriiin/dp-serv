package apiserver

import (
	"github.com/goriiin/dp-serv/internal/store"
	"github.com/gorilla/mux"
	"go.uber.org/zap"
	"io"
	"net/http"
)

type APIServer struct {
	config *Config
	logger *zap.Logger
	router *mux.Router
	store  *store.Store
}

func New(config *Config) *APIServer {
	return &APIServer{
		config: config,
		logger: zap.NewExample(),
		router: mux.NewRouter(),
	}
}

func (s *APIServer) Start() error {
	if err := s.configureLogger(); err != nil {
		return err
	}

	s.configureRouter()

	if err := s.configureStore(); err != nil {
		return err
	}

	s.logger.Info("starting API server")
	return http.ListenAndServe(s.config.BindAddr, s.router)
}

func (s *APIServer) configureLogger() error {
	_, err := zap.ParseAtomicLevel(s.config.LogLevel)
	if err != nil {
		return err
	}

	s.logger.Level()
	return nil
}

func (s *APIServer) configureRouter() {
	s.router.HandleFunc("/", s.HandleTest())
}

func (s *APIServer) configureStore() error {
	st := store.New(s.config.Store)
	if err := st.Open(); err != nil {
		return err
	}
	s.store = st

	return nil
}

func (s *APIServer) HandleTest() http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {
		io.WriteString(w, "TEST")
	}
}
