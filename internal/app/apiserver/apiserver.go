package apiserver

import (
	"go.uber.org/zap"
)

type APIServer struct {
	config *Config
	logger *zap.Logger
}

func New(config *Config) *APIServer {
	return &APIServer{
		config: config,
		logger: zap.NewExample(),
	}
}

func (s *APIServer) Start() error {
	if err := s.configureLogger(); err != nil {
		return err
	}

	s.logger.Info("starting API server")
	return nil
}

func (s *APIServer) configureLogger() error {
	_, err := zap.ParseAtomicLevel(s.config.LogLevel)
	if err != nil {
		return err
	}

	s.logger.Level()
	return nil
}
