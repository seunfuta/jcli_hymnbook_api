import React, { useState } from 'react';
import { Search, Music, AlertCircle } from 'lucide-react';

const HymnSearchApp = () => {
  const [hymnNumber, setHymnNumber] = useState('');
  const [hymn, setHymn] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_BASE_URL = 'http://127.0.0.1:8000';

  const fetchHymnById = async (id) => {
    setLoading(true);
    setError('');
    setHymn(null);

    try {
      const response = await fetch(`${API_BASE_URL}/hymns/${id}`);
      
      if (!response.ok) {
        if (response.status === 404) {
          throw new Error('Hymn not found');
        }
        throw new Error('Failed to fetch hymn');
      }

      const data = await response.json();
      setHymn(data);
    } catch (err) {
      setError(err.message || 'An error occurred while fetching the hymn');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    if (e) e.preventDefault();
    
    const id = parseInt(hymnNumber, 10);
    if (isNaN(id) || id <= 0) {
      setError('Please enter a valid hymn number');
      return;
    }

    fetchHymnById(id);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-2">
            <Music className="w-10 h-10 text-indigo-600" />
            <h1 className="text-4xl font-bold text-gray-800">Hymn Finder</h1>
          </div>
          <p className="text-gray-600">Search for hymns by number</p>
        </div>

        {/* Search Form */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex gap-3">
            <div className="flex-1">
              <input
                type="number"
                value={hymnNumber}
                onChange={(e) => setHymnNumber(e.target.value)}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    handleSubmit(e);
                  }
                }}
                placeholder="Enter hymn number..."
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                min="1"
              />
            </div>
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="px-6 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors flex items-center gap-2 font-medium"
            >
              <Search className="w-5 h-5" />
              {loading ? 'Searching...' : 'Search'}
            </button>
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6 flex items-start gap-3">
            <AlertCircle className="w-5 h-5 text-red-600 mt-0.5 flex-shrink-0" />
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {/* Hymn Display */}
        {hymn && (
          <div className="bg-white rounded-lg shadow-lg p-8">
            {/* Hymn Header */}
            <div className="border-b border-gray-200 pb-4 mb-6">
              <div className="flex items-start justify-between mb-2">
                <h2 className="text-3xl font-bold text-gray-800">{hymn.title}</h2>
                <span className="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm font-semibold">
                  #{hymn.id}
                </span>
              </div>
              <div className="flex gap-3 text-sm">
                <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full">
                  {hymn.language}
                </span>
                <span className="bg-green-100 text-green-800 px-3 py-1 rounded-full">
                  {hymn.group}
                </span>
              </div>
            </div>

            {/* Tune Link */}
            {hymn.tunelink && (
              <div className="mb-6">
                <a
                  href={hymn.tunelink}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-indigo-600 hover:text-indigo-800 underline flex items-center gap-2"
                >
                  <Music className="w-4 h-4" />
                  Listen to tune
                </a>
              </div>
            )}

            {/* Verses */}
            {hymn.verses && hymn.verses.length > 0 && (
              <div className="mb-6">
                <h3 className="text-xl font-semibold text-gray-700 mb-4">Verses</h3>
                {hymn.verses.map((verse, idx) => (
                  <div key={idx} className="mb-4 pl-4 border-l-4 border-indigo-300">
                    <p className="text-sm font-semibold text-gray-500 mb-2">Verse {idx + 1}</p>
                    <div className="space-y-1">
                      {Array.isArray(verse) ? ( 
                        verse.map((line, lineIdx) => (
                          <p key={lineIdx} className="text-gray-700 leading-relaxed">
                            {line}
                          </p>
                        ))
                      ) : (
                        <p className="text-gray-700 leading-relaxed">{verse}</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Chorus */}
            {hymn.chorus && (
              <div className="mb-6 bg-indigo-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-indigo-800 mb-3">Chorus</h3>
                <div className="space-y-1">
                  {Array.isArray(hymn.chorus) ? (
                    hymn.chorus.map((line, idx) => (
                      <p key={idx} className="text-gray-700 leading-relaxed">
                        {line}
                      </p>
                    ))
                  ) : (
                    <p className="text-gray-700 leading-relaxed whitespace-pre-line">
                      {hymn.chorus}
                    </p>
                  )}
                </div>
              </div>
            )}

            {/* Added Chorus */}
            {hymn.addedChorus && (
              <div className="bg-purple-50 p-4 rounded-lg">
                <h3 className="text-xl font-semibold text-purple-800 mb-3">Added Chorus</h3>
                <div className="space-y-1">
                  {Array.isArray(hymn.addedChorus) ? (
                    hymn.addedChorus.map((line, idx) => (
                      <p key={idx} className="text-gray-700 leading-relaxed">
                        {line}
                      </p>
                    ))
                  ) : (
                    <p className="text-gray-700 leading-relaxed whitespace-pre-line">
                      {hymn.addedChorus}
                    </p>
                  )}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Empty State */}
        {!hymn && !error && !loading && (
          <div className="bg-white rounded-lg shadow-lg p-12 text-center">
            <Music className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-500 text-lg">Enter a hymn number to get started</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;